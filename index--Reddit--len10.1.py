# Importando o PySimpleGUI 9Instalado Man.
import PySimpleGUI as sg

# Modelo utilizado (Pegado na bibli)
sg.theme('Reddit')

# Layout da tabela
layout = [
    [sg.Text('Digite seu peso (Kg) e altura (M):')],
    [sg.Text('Peso:'), sg.Input(key='peso')],
    [sg.Text('Altura:'), sg.Input(key='altura')],
    [sg.Button('Calcular')],
    [sg.Text('IMC:', size=(10,1)), sg.Text('', key='imc')],
]

# Criando a janea
window = sg.Window('Saca a Calculadora de IMC', layout)

# Loop para capturar eventos da janela criada.
while True:
    event, values = window.read()
    
    # Verificar se clicou no botão 'Calcular'
    if event == 'Calcular':
        # Calculando o IMC
        peso = float(values['peso'])
        altura = float(values['altura'])
        imc = peso / (altura ** 2)
        imc_formatado = "{:.2f}".format(imc)
        
        # Exibindo o resultado na tabela
        window['imc'].update(imc_formatado)
    
    # Verificando se o usuário fechou a janela
    if event == sg.WINDOW_CLOSED:
        break

# Fechando a janela
window.close()
