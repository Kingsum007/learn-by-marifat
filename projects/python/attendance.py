"""Offline attendance CSV analyst. python attendance.py input.csv report.csv"""
import argparse
import csv
from datetime import date
from pathlib import Path
import re

FIELDS = ['student_id', 'date', 'present']


def read_attendance(path):
    records, seen = [], set()
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream, strict=True)
        if reader.fieldnames != FIELDS:
            raise ValueError('Expected header student_id,date,present')
        for number, row in enumerate(reader, 2):
            if set(row) != set(FIELDS) or any(value is None for value in row.values()):
                raise ValueError(f'Row {number}: incorrect column count')
            student, day, present = (row[key] for key in FIELDS)
            if not re.fullmatch(r'[A-Za-z0-9_-]{1,32}', student):
                raise ValueError(f'Row {number}: invalid student ID')
            try:
                if date.fromisoformat(day).isoformat() != day:
                    raise ValueError('Noncanonical date')
            except ValueError as error:
                raise ValueError(f'Row {number}: invalid YYYY-MM-DD date') from error
            if present not in ('0', '1'):
                raise ValueError(f'Row {number}: present must be 0 or 1')
            if (student, day) in seen:
                raise ValueError(f'Row {number}: duplicate student/date')
            seen.add((student, day))
            records.append((student, day, int(present)))
    return records


def summarize(records):
    """Denominator = this student's recorded sessions, not all calendar days."""
    totals = {}
    for student, _, present in records:
        attended, sessions = totals.get(student, (0, 0))
        totals[student] = attended + present, sessions + 1
    return [(student, attended, sessions, round(100 * attended / sessions, 2))
            for student, (attended, sessions) in sorted(totals.items())]


def export_report(path, rows):
    with Path(path).open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['student_id', 'attended', 'sessions', 'percent'])
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    try:
        if args.input.resolve() == args.output.resolve():
            raise ValueError('Output must differ from input')
        # Parse and validate fully before opening the report for writing.
        rows = summarize(read_attendance(args.input))
        export_report(args.output, rows)
        print(f'{len(rows)} students; header-only report means no recorded sessions.')
    except (ValueError, OSError, csv.Error) as error:
        parser.exit(2, f'Error: {error}\n')


if __name__ == '__main__':
    main()
