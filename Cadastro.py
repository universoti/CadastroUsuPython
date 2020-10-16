from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

layout=[
    [sg.Text('Nome do Usuário'),sg.Input(key='nome',size=(20,1))],
    [sg.Text('Senha do Usuário'),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Text('Departamento'),sg.Input(key='depart')],
    [sg.Button('Salvar')],

]

janela=sg.Window('Tela de Cadastro',layout)
while True:
    eventos, valores=janela.read()
    if eventos==sg.WINDOW_CLOSED:
        break
    
    if eventos=='Salvar':
        print('Usuario cadastro com sucesso!'+valores['nome'])
