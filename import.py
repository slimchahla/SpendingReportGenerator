import csv
import sqlite3

conn = sqlite3.connect('finances.db')

# date, category, amount
# yyyy-mm-dd, int, int
try:
    with open('income.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        income = ((date, category, int(float(amount) * 100)) for date, category, amount in reader)
        conn.executemany('INSERT INTO income(date, category, amount) VALUES (?, ?, ?)', income)
except FileNotFoundError:
    pass

# date, category, amount
# yyyy-mm-dd, int, int
try:
    with open('investments.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        income = ((date, category, int(float(amount) * 100)) for date, category, amount in reader)
        conn.executemany('INSERT INTO investments(date, category, amount) VALUES (?, ?, ?)', income)
except FileNotFoundError:
    pass

# date, card, amount, description category
# yyyy-mm-dd, string, int, string, int
try:
    with open('purchases.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        income = ((date, card, int(float(amount) * 100), description, category) for
                  date, card, amount, description, category in reader)
        conn.executemany('INSERT INTO purchases(date, card, amount, description, category) VALUES (?, ?, ?, ?, ?)',
                         income)
except FileNotFoundError:
    pass

conn.commit()
conn.close()
