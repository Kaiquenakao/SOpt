import PySimpleGUI as sg  
  
def telaPython():  
    layout = [  
            [sg.Text('Quanto você ganhou hoje?')],  
            [sg.Text('Data:   '), sg.Input(size=(16, 0), key='data')],  
            [sg.Text('Ganhos:'),sg.Input(size=(15,3), key='ganhos')],  
            [sg.Text('Gastos:'), sg.Input(size=(15,0),key='gastos')],  
            [sg.Button('Calcular', key='calcular')]  
    ]  
  
    return sg.Window("Dados do Usuário", layout, finalize=True)  
  
janela = telaPython()  
  
while True:  
    window, event, values = sg.read_all_windows()  
    if event == sg.WINDOW_CLOSED:  
        break  
  
     if event == 'calcular':  
        print(f'data: {values["data"]}')  
        print(f'ganhos: {values["ganhos"]}')  
        print(f'gastos: {values["gastos"]}')