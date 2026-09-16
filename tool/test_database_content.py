"""Execute self-contained relational lesson scripts using real SQLite."""
import sqlite3
import unittest
from database_courses import COURSES

EXPECTED={
 'database-foundations':[[('Python',100),('Databases',150),('Web',100)],[(1,'Python basics'),(2,'Databases'),(3,'Web')],[('Databases',)],[('Python','Computing'),('Web','Computing')],[('Amina',20)],[(100,)]],
 'sql':[[('Python',),('Databases',),('Web',)],[('Databases',150),('Python',100)],[(100,2),(150,1)],[('Python',2),('Databases',0),('Web',0)],[('Python','No note'),('Databases','No note'),('Web','No note')],[(1,120),(2,150),(3,100)]],
 'sqlite':[[(3,)],[('Python','integer'),('Databases','integer'),('Web','integer')],[(90,)],None,[(1,1),(2,1),(3,1)],[(3,350)]]
}

class DatabaseLessons(unittest.TestCase):
    def test_all_relational_examples(self):
        for course in COURSES:
            if course['id'] not in EXPECTED: continue
            for i,module in enumerate(course['modules']):
                with self.subTest(course=course['id'],module=i+1),sqlite3.connect(':memory:',isolation_level=None) as db:
                    statements=module['code'].split(';')
                    outputs=[]
                    for statement in statements:
                        if statement.strip():
                            cursor=db.execute(statement)
                            if cursor.description: outputs.append(cursor.fetchall())
                    self.assertTrue(outputs)
                    expected=EXPECTED[course['id']][i]
                    if expected is not None: self.assertEqual(outputs[-1],expected)
                    if course['id']=='sqlite' and i==5:self.assertEqual(outputs[-2],[('ok',)])

    def test_integrity_rules(self):
        with sqlite3.connect(':memory:') as db:
            db.execute('PRAGMA foreign_keys=ON')
            db.executescript(COURSES[0]['modules'][2]['code'])
            with self.assertRaises(sqlite3.IntegrityError):db.execute('INSERT INTO loans VALUES(2,99)')
            with self.assertRaises(sqlite3.IntegrityError):db.execute("INSERT INTO books VALUES(1,'Duplicate',10)")
            with self.assertRaises(sqlite3.IntegrityError):db.execute("INSERT INTO books VALUES(4,'Invalid',-1)")

if __name__=='__main__':unittest.main()
