"""Offline transactional shop. python inventory.py --help"""
import argparse
import json
from pathlib import Path
import sqlite3


class Inventory:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.execute('PRAGMA foreign_keys=ON')
        with self.db:
            self.db.execute('CREATE TABLE IF NOT EXISTS items (sku TEXT PRIMARY KEY, stock INTEGER NOT NULL CHECK(stock>=0))')
            self.db.execute('CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY, sku TEXT NOT NULL REFERENCES items(sku), quantity INTEGER NOT NULL CHECK(quantity>0))')

    def close(self):
        self.db.close()

    def add(self, sku, stock):
        if not isinstance(sku, str) or not sku.strip() or type(stock) is not int or stock < 0:
            raise ValueError('Use a nonblank SKU and nonnegative integer stock')
        with self.db:
            self.db.execute('INSERT INTO items VALUES (?, ?)', (sku.strip(), stock))

    def sell(self, sku, quantity):
        if type(quantity) is not int or quantity <= 0:
            raise ValueError('Sale quantity must be a positive integer')
        # A single conditional UPDATE prevents overselling across connections.
        # The sales INSERT and stock UPDATE commit or roll back together.
        with self.db:
            changed = self.db.execute('UPDATE items SET stock=stock-? WHERE sku=? AND stock>=?', (quantity, sku, quantity))
            if changed.rowcount != 1:
                raise ValueError('Unknown SKU or insufficient stock')
            self.db.execute('INSERT INTO sales(sku,quantity) VALUES (?,?)', (sku, quantity))

    def low_stock(self, threshold=3):
        if type(threshold) is not int or threshold < 0:
            raise ValueError('Threshold must be a nonnegative integer')
        return self.db.execute('SELECT sku,stock FROM items WHERE stock<=? ORDER BY sku', (threshold,)).fetchall()

    def snapshot(self):
        # One read transaction gives a consistent items/sales snapshot.
        self.db.execute('BEGIN')
        try:
            return {'items': [{'sku': sku, 'stock': stock} for sku, stock in self.db.execute('SELECT sku,stock FROM items ORDER BY sku')],
                    'sales': [{'id': id_, 'sku': sku, 'quantity': qty} for id_, sku, qty in self.db.execute('SELECT id,sku,quantity FROM sales ORDER BY id')]}
        finally:
            self.db.rollback()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=Path('shop.sqlite'))
    commands = parser.add_subparsers(dest='command', required=True)
    add = commands.add_parser('add'); add.add_argument('sku'); add.add_argument('stock', type=int)
    sell = commands.add_parser('sell'); sell.add_argument('sku'); sell.add_argument('quantity', type=int)
    low = commands.add_parser('low'); low.add_argument('--threshold', type=int, default=3)
    export = commands.add_parser('export'); export.add_argument('output', type=Path)
    args = parser.parse_args()
    store = None
    try:
        if args.command == 'export' and args.output.resolve() == args.db.resolve():
            raise ValueError('Export must not replace the database')
        store = Inventory(args.db)
        if args.command == 'add': store.add(args.sku, args.stock)
        elif args.command == 'sell': store.sell(args.sku, args.quantity)
        elif args.command == 'low': print(json.dumps(store.low_stock(args.threshold), ensure_ascii=False))
        else: args.output.write_text(json.dumps(store.snapshot(), ensure_ascii=False, indent=2), encoding='utf-8')
    except (ValueError, OSError, sqlite3.Error) as error:
        parser.exit(2, f'Error: {error}\n')
    finally:
        if store is not None: store.close()


if __name__ == '__main__':
    main()
