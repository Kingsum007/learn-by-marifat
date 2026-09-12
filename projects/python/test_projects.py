import csv
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
import subprocess
import sys
from unittest.mock import patch
from expense_ledger import load, save, validate, weekly
from attendance import read_attendance, summarize, export_report
from inventory import Inventory


class ProjectsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
    def tearDown(self):
        self.temp.cleanup()
    def expense(self, day='2026-09-12', category='Food', amount=20):
        return {'date': day, 'category': category, 'amount': amount}
    def csv(self, text):
        path = self.root / 'input.csv'
        path.write_text(text, encoding='utf-8')
        return path
    def cli(self, name, *args):
        return subprocess.run([sys.executable, str(Path(__file__).parent/name), *args], cwd=self.root, capture_output=True, text=True, encoding='utf-8')
    def test_ledger_cli_add_and_report(self):
        self.assertEqual(self.cli('expense_ledger.py','add','2026-09-12','Food','20').returncode,0)
        result=self.cli('expense_ledger.py','report','2026-09-12')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads(result.stdout)['total'],20)
    def test_attendance_cli_invalid_input_preserves_report(self):
        source=self.csv('student_id,date,present\nS1,2026-09-12,1\n')
        output=self.root/'report.csv'
        result=self.cli('attendance.py',str(source),str(output))
        self.assertEqual(result.returncode,0,result.stderr)
        original=output.read_bytes()
        source.write_text('bad header',encoding='utf-8')
        self.assertEqual(self.cli('attendance.py',str(source),str(output)).returncode,2)
        self.assertEqual(output.read_bytes(),original)
        self.assertEqual(self.cli('attendance.py',str(source),str(source)).returncode,2)
    def test_inventory_cli_export_and_protect_database(self):
        self.assertEqual(self.cli('inventory.py','add','Pen','5').returncode,0)
        self.assertEqual(self.cli('inventory.py','sell','Pen','2').returncode,0)
        output=self.root/'snapshot.json'
        result=self.cli('inventory.py','export',str(output))
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads(output.read_text())['items'],[{'sku':'Pen','stock':3}])
        self.assertEqual(self.cli('inventory.py','export','shop.sqlite').returncode,2)
        self.assertEqual(self.cli('inventory.py','sell','Pen','99').returncode,2)
        self.assertEqual(json.loads(self.cli('inventory.py','low').stdout),[['Pen',3]])
    def test_ledger_week_boundary_and_categories(self):
        rows = [self.expense(), self.expense(amount=30), self.expense(category='Travel', amount=10),
                self.expense(day='2026-09-19', amount=999), self.expense(day='2026-09-11', amount=999)]
        self.assertEqual(weekly(rows, '2026-09-12'), {'categories': {'Food':50, 'Travel':10}, 'total':60})
        self.assertEqual(weekly([], '2026-09-12')['total'], 0)
    def test_ledger_restart_unicode(self):
        path = self.root / 'ledger.json'
        self.assertEqual(load(path), [])
        rows = [self.expense(category='خواړه')]
        save(path, rows)
        self.assertEqual(load(path), rows)
    def test_ledger_rejects_bad_records_without_overwrite(self):
        path = self.root / 'ledger.json'
        save(path, [self.expense()]); original = path.read_bytes()
        for row in [self.expense(amount=-1), self.expense(amount=True), self.expense(category='  '),
                    self.expense(day='2026-02-30'), self.expense(amount=1.5), {'date':'2026-09-12'}]:
            with self.subTest(row=row), self.assertRaises((ValueError, TypeError)):
                save(path, [row])
            self.assertEqual(path.read_bytes(), original)
    def test_ledger_failed_replace_retains_original_and_cleans_temp(self):
        path = self.root / 'ledger.json'; save(path, [self.expense()])
        original = path.read_bytes()
        with patch('expense_ledger.os.replace', side_effect=OSError('Simulated disk failure')):
            with self.assertRaises(OSError): save(path, [self.expense(amount=100)])
        self.assertEqual(path.read_bytes(), original)
        self.assertEqual(list(self.root.iterdir()), [path])
    def test_ledger_malformed_json(self):
        path = self.root / 'ledger.json'; path.write_text('{bad', encoding='utf-8')
        with self.assertRaises(ValueError): load(path)
        with self.assertRaises(ValueError): validate({})
    def test_attendance_percentage_and_empty_rule(self):
        path = self.csv('student_id,date,present\nS1,2026-09-12,1\nS1,2026-09-13,0\nS2,2026-09-12,1\n')
        self.assertEqual(summarize(read_attendance(path)), [('S1',1,2,50.0),('S2',1,1,100.0)])
        self.assertEqual(summarize([]), [])
        out=self.root/'report.csv'; export_report(out,[])
        self.assertEqual(list(csv.reader(out.read_text(encoding='utf-8').splitlines())), [['student_id','attended','sessions','percent']])
    def test_attendance_rejects_duplicate_invalid_and_malformed(self):
        header='student_id,date,present\n'
        invalid=['S1,2026-09-12,1\nS1,2026-09-12,0\n','S1,2026-02-30,1\n',',2026-09-12,1\n',
                 'S1,2026-09-12,2\n','S1,2026-09-12\n','S1,2026-09-12,1,extra\n','"S1,2026-09-12,1\n']
        for body in invalid:
            with self.subTest(body=body), self.assertRaises((ValueError,csv.Error)):
                read_attendance(self.csv(header+body))
        with self.assertRaises(ValueError): read_attendance(self.csv('wrong,header\n'))
    def test_attendance_utf8_export(self):
        out=self.root/'report.csv'; export_report(out,[('S1',2,3,66.67)])
        self.assertIn('S1,2,3,66.67',out.read_text(encoding='utf-8'))
    def test_inventory_restart_and_reports(self):
        path=self.root/'shop.sqlite'; store=Inventory(path)
        store.add('Pen',5);store.sell('Pen',2);store.close()
        store=Inventory(path)
        try:
            self.assertEqual(store.low_stock(), [('Pen',3)])
            snapshot=store.snapshot()
            self.assertEqual(snapshot['sales'][0]['quantity'],2)
            self.assertEqual(json.loads(json.dumps(snapshot))['items'],[{'sku':'Pen','stock':3}])
        finally: store.close()
    def test_inventory_rejects_oversale_and_invalid_input(self):
        store=Inventory(':memory:')
        try:
            store.add('Pen',2)
            for sku,quantity in [('Pen',3),('Pen',0),('Pen',-1),('Missing',1),('Pen',True)]:
                with self.assertRaises(ValueError): store.sell(sku,quantity)
            self.assertEqual(store.snapshot(), {'items':[{'sku':'Pen','stock':2}], 'sales':[]})
            with self.assertRaises(sqlite3.IntegrityError): store.add('Pen',8)
        finally: store.close()
    def test_inventory_insert_failure_rolls_back_stock(self):
        store=Inventory(':memory:')
        try:
            store.add('Pen',5)
            store.db.execute("CREATE TRIGGER reject_sale BEFORE INSERT ON sales BEGIN SELECT RAISE(ABORT, 'simulated'); END")
            with self.assertRaises(sqlite3.IntegrityError): store.sell('Pen',2)
            self.assertEqual(store.low_stock(5), [('Pen',5)])
            self.assertEqual(store.snapshot()['sales'],[])
        finally: store.close()
    def test_inventory_second_connection_cannot_oversell(self):
        path=self.root/'shop.sqlite'; first=Inventory(path);second=Inventory(path)
        try:
            first.add('Pen',3);first.sell('Pen',2)
            with self.assertRaises(ValueError): second.sell('Pen',2)
            self.assertEqual(second.low_stock(),[('Pen',1)])
        finally: first.close();second.close()

if __name__ == '__main__':
    unittest.main()
