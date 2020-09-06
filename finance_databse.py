from typing import List, Tuple

import sqlite3

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

class Database:

    def __init__(self, database_name='finances.db'):
        self.conn = sqlite3.connect(database_name)
        self.transaction_types = ('Income', 'Investment', 'Purchases')

    def get_categories(self, table: str) -> List[str]:
        query = 'SELECT name FROM categories WHERE type = ? ORDER BY name'
        cats = [r[0] for r in self.conn.execute(query, (self.transaction_types.index(table),))]
        return cats

    def get_payment_methods(self) -> List[str]:
        methods = [r[0] for r in self.conn.execute('SELECT name FROM payment_method ORDER BY name')]
        return methods

    def get_monthly_spending(self, year: str, month: str) -> List[Tuple]:
        month_num = MONTHS.index(month) + 1
        query = '''SELECT categories.name, sum(purchases.amount)/100 
                   FROM purchases JOIN categories ON purchases.category = categories.id
                   WHERE date LIKE ? GROUP BY category ORDER BY category'''
        return [r for r in self.conn.execute(query, (f'{year}-{month_num:02d}-%',))]

    def get_yearly_spending(self, year: str) -> List[Tuple]:
        query = '''SELECT categories.name, sum(purchases.amount)/100 
                   FROM purchases JOIN categories ON purchases.category = categories.id
                   WHERE date LIKE ? GROUP BY category ORDER BY category'''
        return [r for r in self.conn.execute(query, (f'{year}-%',))]
