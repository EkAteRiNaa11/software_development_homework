"""
Рожнова Екатерина Александровна
Группа 44-22-112
Вариант 21
"""

import PySimpleGUI as sg
from expression import expression


layout = [
    [sg.Text("Введите данные для функции через пробел")],
    [sg.Input(enable_events=True, key="-INPUT-")],
    [sg.Button("Вычислить")],
    [sg.Listbox(values=[], enable_events=True, key="-LISTBOX-", size=(80, 40))]
]

window = sg.Window("Вычислить значение функции", layout, font=("Arial, 12"))

while True:
    event, values = window.read()
    if event == "Вычислить":
        args = values['-INPUT-'].strip().split(" ")
        results, logs = expression(*args)
        window["-LISTBOX-"].update(logs)
    if event == sg.WIN_CLOSED:
        break

window.close()