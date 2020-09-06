import finance_databse
import PySimpleGUI as sg
import datetime
import re

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

db = finance_databse.Database()


def get_current_date() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d')


def check_date_format(date: str) -> bool:
    return re.match('\\d{4}-\\d{2}-\\d{2}', date)


purchase_layout = [[sg.Text('Date'), sg.InputText(get_current_date())],
                   [sg.Text('Payment Method'), sg.Combo(db.get_payment_methods(), key='purchase_card')],
                   [sg.Text('Amount'), ]]

main_layout = [[sg.Radio('Purchase', 'GROUP1', default=True, enable_events=True, key='radio_purchase'),
                sg.Radio('Income', 'GROUP1', enable_events=True, key='radio_income'),
                sg.Radio('Investment', 'GROUP1', enable_events=True, key='radio_invest')],
               [sg.Frame('Add Purchase', purchase_layout)]
               ]

window = sg.Window('Add Transaction', main_layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break

window.close()
