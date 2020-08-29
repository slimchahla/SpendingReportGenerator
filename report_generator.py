from typing import List, Tuple
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import datetime
import sqlite3

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

conn = sqlite3.connect('finances.db')


def get_current_year() -> str:
    return datetime.datetime.now().strftime('%Y')


def get_current_month() -> str:
    return datetime.datetime.now().strftime('%B')


def get_monthly_categories(year: str, month: str) -> List[str]:
    month_num = MONTHS.index(month) + 1
    query = 'SELECT DISTINCT category FROM purchases WHERE date LIKE ? ORDER BY category'
    return [r[0] for r in conn.execute(query, (f'{year}-{month_num:02d}-%',))]


def get_monthly_spending(year: str, month: str):
    month_num = MONTHS.index(month) + 1
    query = '''SELECT categories.name, sum(purchases.amount)/100 
               FROM purchases JOIN categories ON purchases.category = categories.id
               WHERE date LIKE ? GROUP BY category ORDER BY category'''
    rows = [r for r in conn.execute(query, (f'{year}-{month_num:02d}-%',))]
    create_spending_report(rows)


def get_yearly_spending(year: str):
    query = '''SELECT categories.name, sum(purchases.amount)/100 
               FROM purchases JOIN categories ON purchases.category = categories.id
               WHERE date LIKE ? GROUP BY category ORDER BY category'''
    rows = [r for r in conn.execute(query, (f'{year}-%',))]
    create_spending_report(rows)


def create_spending_report(rows: List[Tuple]):
    categories = [r[0] for r in rows]
    amounts = [r[1] for r in rows]

    make_pie_chart(amounts, categories)


def make_pie_chart(amounts: List[int], labels: List[str]):
    fig, ax = plt.subplots()
    ax.pie(amounts, labels=labels, autopct='%1.1f%%', normalize=True)
    ax.axis('equal')
    plt.tight_layout()
    plt.show()


layout = [[sg.Text('Generate Spending Report')],
          [sg.Text('Month'), sg.Combo(MONTHS, default_value=get_current_month(), key='month'),
           sg.Text('Year'),
           sg.Spin([i for i in range(1900, 9999)], initial_value=get_current_year(), key='year')],
          [sg.Button('Generate Monthly', key='generate_monthly')],
          [sg.Button('Generate Yearly', key='generate_yearly')]
          ]

# Create the Window
window = sg.Window('Finances', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'generate_monthly':
        get_monthly_spending(values['year'], values['month'])
    elif event == 'generate_yearly':
        get_yearly_spending(values['year'])
    elif event == sg.WIN_CLOSED:
        break

window.close()
