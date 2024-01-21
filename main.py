#Passo a passo do projeto


# Passo 1 - Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time


pyautogui.PAUSE = 0.3

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# clicar -> pyautogui.click()
# escrever -> pyautogui.write()
# apertar uma tecla -> pyautogui.press()
# apertar -> pyautogui.hotkey()
# scroll -> pyautogui.scroll()



pyautogui.press('win')

pyautogui.write('opera')

pyautogui.press('enter')

pyautogui.click(x=350, y=64)

pyautogui.hotkey('ctrl' + 'a')

pyautogui.write(link)

pyautogui.press('enter')

#esperar 5 segundos APENAS NESSA LINHA

time.sleep(5)


# Passo 2 - Fazer login

pyautogui.click(x=815, y=388)

# Digitar email

pyautogui.write('gabriel.benini2@gmail.com')

pyautogui.press('tab')

pyautogui.write('Gabriel@11298')

pyautogui.click(x=977, y=546)

time.sleep(3)

# Passo 3 - Importar base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)


for linha in tabela.index: #index sao as linhas, collumns as colunas...

    # Passo 4 - Cadastrar um produto

    pyautogui.click(x=757, y=270)

    # Codigo
    codigo = tabela.loc[linha, 'codigo']    #[linha, coluna]
    pyautogui.write(codigo)                 #pyautogui.write(tabela.loc[linha, 'codigo'] ) <-- outra opcao
    pyautogui.press('tab')

    # Marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    # Tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    # Categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria'])) # '1'
    pyautogui.press('tab')

    # Preco unitario
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    # Custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    #obs

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):        #"Se o panda nao estiver vazio"
        pyautogui.write(obs)

    #enviar o produto

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(1000)


# Passo 5 - Repetir isso ate acabar a base de dados