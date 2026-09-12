# Python project reference pack

These are complete **command-line reference applications** for the three Python capstone briefs. They use only the CPython standard library. They are educational examples with fictional data, not production accounting or school administration systems.

The Flutter app contains their source, run commands, six-stage Bloom walkthroughs in English/Dari/Pashto, and smaller executable practice functions. The full file/SQLite programs require CPython on a computer; the app's teaching interpreter cannot run imports, CSV, JSON files, or SQLite.

## First run

1. Provision CPython before going offline. This pack was tested with CPython 3.14.7 on Windows. No pip dependencies are needed.
2. Put the three `.py` programs and `test_projects.py` in one folder. Open a terminal in that folder. `python --version` should identify Python 3.
3. Run `python -m unittest discover -s . -p test_projects.py -v`. The 15 tests use temporary directories and fictional data.
4. Copy the commands below one line at a time. Inspect created files with a text editor. Repeat the commands with changed inputs and explain each difference.

## 1. Household expense ledger

A record has exactly `date`, `category`, and `amount`. Dates use YYYY-MM-DD, categories cannot be blank, and amounts are nonnegative integer AFN. Boolean values are not accepted as amounts. A week is seven days starting at the date requested; it need not start on Monday. Category names are case-sensitive after trimming spaces.

```text
python expense_ledger.py add 2026-09-12 Food 20
python expense_ledger.py add 2026-09-13 Food 30
python expense_ledger.py add 2026-09-14 Travel 10
python expense_ledger.py report 2026-09-12
```

The report has Food=50, Travel=10, total=60. Add a record on 2026-09-19; it must not change that week's report. A negative amount or malformed JSON must be rejected. Running the same `add` twice adds two expenses; it is not an idempotent import.

Architecture decision: validation and weekly calculations are pure functions; file persistence is a separate adapter. Validate the complete batch, write a temporary file beside the destination, then replace it atomically. A failure before replacement retains the last valid ledger. This design does not support concurrent ledger writers; use one instance at a time. It does not claim power-loss guarantees for directory metadata on every filesystem.

## 2. School attendance analyst

Create `attendance.csv` in a text editor:

```csv
student_id,date,present
S1,2026-09-12,1
S1,2026-09-13,0
S2,2026-09-12,1
```

Run `python attendance.py attendance.csv report.csv`. S1 is 1/2=50%, S2 is 1/1=100%. Inspect `report.csv`.

The denominator is **recorded sessions for that student**. A missing row is unknown, not an automatic absence. Header-only input creates a header-only report, with no invented 0% values. Student IDs use 1–32 ASCII letters, digits, `_` or `-`. Dates must be valid and canonical. Duplicate student/date pairs and markers other than 0/1 are rejected, including conflicting duplicates. Incorrect column counts and malformed quoted CSV are rejected. Export uses UTF-8.

Architecture decision: parse and validate the whole input before opening the report, so invalid input cannot replace a previous report. This small educational implementation holds all records in memory and has no roster/calendar reconciliation. Report writing is not an atomic durability guarantee: an I/O failure during export can leave a partial report, which can be regenerated from the unchanged CSV.

## 3. Community shop inventory

```text
python inventory.py add Pen 5
python inventory.py sell Pen 2
python inventory.py low
python inventory.py export snapshot.json
python inventory.py sell Pen 99
```

The low-stock report shows Pen=3. The final command fails and must leave both stock and sale history unchanged. Close the terminal, open it again in the same folder and run `python inventory.py low` to verify persistence. Run the regression suite for an injected sale-insert failure and rollback.

Architecture decision: SQLite owns stock/sales persistence. A conditional UPDATE and sale INSERT run in one transaction. Conditional update prevents a second connection selling based on outdated stock. Database CHECK constraints preserve nonnegative stock and positive quantities; bound SQL parameters separate values from commands. Snapshot uses a read transaction for a consistent report. Duplicate SKU creation is rejected; this version does not implement restocking, pricing, authentication, or returns. JSON export is a report, not an importable database backup.

## Learning sequence and assessment

For each project: define the terms; predict and trace a normal example; implement the in-app function; deliberately introduce the documented bug; compare the reference architecture with a simpler alternative; create and test your own extension. Record expected/actual output, a failure, its cause, the fix, and a regression test. Passing supplied tests demonstrates those cases, not comprehensive correctness or mastery.

Keep the original project source alongside your version so differences are reviewable. In the app, practice solution loading affects the editor only until explicitly saved; local workspace backups include your saved source and notes.
