"""Authored Python project walkthroughs and executable teaching-core exercises."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GUIDES={
'python-p1': dict(
steps=[
'Remember: an expense is one dated payment. AFN amounts are whole numbers. A list holds several payments; a category groups payments such as food or travel. Finish the foundation lessons on lists, loops, and functions first.',
'Understand: start with [20, 30]. Set total to 0; reading 20 changes it to 20, and reading 30 changes it to 50. An empty list leaves the total at 0. Predict these values before running the code.',
'Apply: complete total_expenses below. Visit every amount. If any amount is negative, return -1 to reject the whole batch; otherwise add it to total and return total after the loop. Return inside the loop only for an invalid value.',
'Analyze: move the final return into the loop deliberately. The [20, 30] case then returns 20. Explain why the second payment was skipped, restore the indentation, and rerun all three cases.',
'Evaluate: the in-app exercise teaches only numeric aggregation and rejection. The complete reference adds date/category validation and atomic JSON replacement. Validate every record before replacing a file so a failed import cannot erase the previous ledger.',
'Create: use the complete reference to add two food payments and one travel payment, then report a seven-day interval. Its first day is included and the eighth day is excluded. Add an outside-week record and demonstrate that the total stays unchanged. Keep your own prediction, actual output, and explanation in TESTS.md.'
],
starter='def total_expenses(amounts):\n    total = 0\n    return total\n\nprint(total_expenses([20, 30]))\nprint(total_expenses([]))\nprint(total_expenses([20, -5]))',
solution='def total_expenses(amounts):\n    total = 0\n    for amount in amounts:\n        if amount < 0:\n            return -1\n        total = total + amount\n    return total\n\nprint(total_expenses([20, 30]))\nprint(total_expenses([]))\nprint(total_expenses([20, -5]))',
expected='50\n0\n-1',file='expense_ledger.py',
commands='python expense_ledger.py add 2026-09-12 Food 20\npython expense_ledger.py add 2026-09-13 Food 30\npython expense_ledger.py add 2026-09-14 Travel 10\npython expense_ledger.py report 2026-09-12',
),
'python-p2':dict(
steps=[
'Remember: one attendance record identifies a student, a date, and whether the student attended. Use 1 for present and 0 for absent. A percentage compares attended sessions with that student\'s recorded sessions.',
'Understand: [1, 0, 1, 1] has four sessions and three attendances. Three divided by four, multiplied by 100, is 75 percent. Do not divide by the number of students or by every day on the calendar.',
'Apply: complete attendance_percent. Count the list length first. Return -1 if the list is empty, meaning no percentage is available. Reject values other than 0 or 1 with -1. Add the remaining values and divide only after the empty case is handled.',
'Analyze: remove the empty-list guard and run the empty example. Explain the division-by-zero failure. Restore the guard, then try [1, 2] to show why a presence marker must be validated before it enters the total.',
'Evaluate: the complete CSV program rejects duplicate student/date rows rather than silently counting a session twice. A header-only input produces a header-only report; a student with no records has no report row. This differs from zero percent, which means recorded sessions were all missed.',
'Create: save a CSV with header student_id,date,present and three fictional records. Run the reference program and inspect the exported UTF-8 report. Add a duplicate row, verify rejection, and confirm that a previously valid report is unchanged. Document the denominator and missing-record limitation.'
],
starter='def attendance_percent(sessions):\n    return 0\n\nprint(attendance_percent([1, 0, 1, 1]))\nprint(attendance_percent([0, 0]))\nprint(attendance_percent([]))\nprint(attendance_percent([1, 2]))',
solution='def attendance_percent(sessions):\n    count = len(sessions)\n    if count == 0:\n        return -1\n    attended = 0\n    for present in sessions:\n        if present != 0 and present != 1:\n            return -1\n        attended = attended + present\n    return attended * 100 / count\n\nprint(attendance_percent([1, 0, 1, 1]))\nprint(attendance_percent([0, 0]))\nprint(attendance_percent([]))\nprint(attendance_percent([1, 2]))',
expected='75.0\n0.0\n-1\n-1',file='attendance.py',
commands='python attendance.py attendance.csv report.csv\n# attendance.csv:\n# student_id,date,present\n# S1,2026-09-12,1\n# S1,2026-09-13,0\n# S2,2026-09-12,1',
),
'python-p3':dict(
steps=[
'Remember: stock is the number of available items. A sale reduces stock. An invariant is a rule that must always hold: stock must never become negative, and a sale quantity must be positive.',
'Understand: with stock 5, selling 2 leaves 3. Selling 6 must fail and leave 5. Separate the decision from storage: first learn a pure function that calculates the next stock without changing any outside value.',
'Apply: complete stock_after_sale. Reject negative stock, zero or negative quantity, and quantities above available stock by returning -1. For a valid sale return stock minus quantity. Selling exactly the available stock should return 0.',
'Analyze: replace quantity > stock with quantity >= stock. The exact-stock sale now fails. Explain the difference between these comparisons, fix it, and retain that example as a regression test.',
'Evaluate: saving stock and recording a sale are one business operation. In the SQLite reference, both statements share a transaction. If recording the sale fails, stock rolls back too. A conditional UPDATE also stops a second connection from overselling stale stock.',
'Create: run the complete shop reference with a fictional Pen item. Sell two, reopen the program, and inspect the low-stock report and JSON export. Attempt an oversale and verify stock and sales remain unchanged. Extend your design with a restock operation and explain which operations must be atomic.'
],
starter='def stock_after_sale(stock, quantity):\n    return stock\n\nprint(stock_after_sale(5, 2))\nprint(stock_after_sale(5, 6))\nprint(stock_after_sale(5, 0))\nprint(stock_after_sale(5, 5))',
solution='def stock_after_sale(stock, quantity):\n    if stock < 0 or quantity <= 0 or quantity > stock:\n        return -1\n    return stock - quantity\n\nprint(stock_after_sale(5, 2))\nprint(stock_after_sale(5, 6))\nprint(stock_after_sale(5, 0))\nprint(stock_after_sale(5, 5))',
expected='3\n-1\n-1\n0',file='inventory.py',
commands='python inventory.py add Pen 5\npython inventory.py sell Pen 2\npython inventory.py low\npython inventory.py export snapshot.json\npython inventory.py sell Pen 99',
)}
for guide in GUIDES.values():
    guide['reference']=(ROOT/'projects/python'/guide['file']).read_text(encoding='utf-8-sig')
(ROOT/'assets/curriculum/project_guides.json').write_text(json.dumps(GUIDES,ensure_ascii=False,indent=2),encoding='utf-8')
payload=json.dumps(GUIDES,ensure_ascii=False,separators=(',',':'))
(ROOT/'lib/data/project_guides.dart').write_text("// Generated by tool/build_project_guides.py.\nimport 'dart:convert';\nimport '../domain/project_guide.dart';\nfinal projectGuides = (jsonDecode(r'''"+payload+"''') as Map<String,dynamic>).map((id,data)=>MapEntry(id,ProjectGuide(data as Map<String,dynamic>)));\n",encoding='utf-8')

test_payload=json.dumps((ROOT/'projects/python/test_projects.py').read_text(encoding='utf-8'),ensure_ascii=False)
with (ROOT/'lib/data/project_guides.dart').open('a',encoding='utf-8') as out:
    out.write("final String projectReferenceTests = jsonDecode(r'''"+test_payload+"''') as String;\n")

with (ROOT/'lib/data/project_guides.dart').open('a',encoding='utf-8') as out:
    out.write("const projectTestCommand = 'python -m unittest discover -s . -p test_projects.py -v';\n")
