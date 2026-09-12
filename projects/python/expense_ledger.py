"""Offline household ledger. python expense_ledger.py --help"""
import argparse
from datetime import date, timedelta
import json
import os
from pathlib import Path
import tempfile


def validate(records):
    if not isinstance(records, list):
        raise ValueError('Ledger must be a list')
    clean = []
    for record in records:
        if not isinstance(record, dict) or set(record) != {'date', 'category', 'amount'}:
            raise ValueError('Every expense needs date, category and amount')
        day, category, amount = record['date'], record['category'], record['amount']
        if not isinstance(day, str) or date.fromisoformat(day).isoformat() != day:
            raise ValueError('Use a valid YYYY-MM-DD date')
        if not isinstance(category, str) or not category.strip():
            raise ValueError('Category cannot be blank')
        if type(amount) is not int or amount < 0:
            raise ValueError('Amount must be a nonnegative integer AFN value')
        clean.append({'date': day, 'category': category.strip(), 'amount': amount})
    return clean


def load(path):
    path = Path(path)
    return validate(json.loads(path.read_text(encoding='utf-8'))) if path.exists() else []


def save(path, records):
    """Validate before writing; replacement is atomic on the same filesystem."""
    text = json.dumps(validate(records), ensure_ascii=False, indent=2)
    path = Path(path)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                         delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def weekly(records, start):
    first = date.fromisoformat(start)
    if first.isoformat() != start:
        raise ValueError('Use YYYY-MM-DD for week start')
    end = first + timedelta(days=7)
    totals = {}
    for record in validate(records):
        if first <= date.fromisoformat(record['date']) < end:
            category = record['category']
            totals[category] = totals.get(category, 0) + record['amount']
    return {'categories': dict(sorted(totals.items())), 'total': sum(totals.values())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file', type=Path, default=Path('expenses.json'))
    commands = parser.add_subparsers(dest='command', required=True)
    add = commands.add_parser('add')
    add.add_argument('date'); add.add_argument('category'); add.add_argument('amount', type=int)
    report = commands.add_parser('report')
    report.add_argument('start', help='First of seven included days: YYYY-MM-DD')
    args = parser.parse_args()
    try:
        records = load(args.file)
        if args.command == 'add':
            save(args.file, records + [{'date': args.date, 'category': args.category, 'amount': args.amount}])
            print('Saved')
        else:
            print(json.dumps(weekly(records, args.start), ensure_ascii=False, indent=2))
    except (ValueError, OSError) as error:
        parser.exit(2, f'Error: {error}\n')


if __name__ == '__main__':
    main()
