import PySimpleGUI as sg

#https://pysimplegui.readthedocs.io/en/latest/

layout = [
    [sg.Text('hello world')]
]

window = sg.Window('OptionsAlgoTrader', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()