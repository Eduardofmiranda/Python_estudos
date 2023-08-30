import time
import pyautogui
import pandas as pd


pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=2147, y=497)
pyautogui.click(x=2633, y=16)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.sleep(5)
pyautogui.click(x=2159, y=360)
pyautogui.write("miranda_eduardo.freitas@hotmail.com")
pyautogui.press("tab")
pyautogui.write("eduardo2023")
pyautogui.click(x=2175, y=528)

tabela = pd.read_csv("produtos.csv")
print(tabela)

#passo 4: Cadastrar um produto
linha = 0
for linha in tabela.index:
    #clicar no campo de codigo
    pyautogui.click(x=2051, y=240)
    #pega o valor do campo que precisa preencher
    codigo = tabela.loc[linha, "codigo"]
    #preenche o campo
    pyautogui.write(str(codigo))
    # Passar para o proximo campo
    pyautogui.press("tab")
    #preenche o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):        
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    # Clica em enviar para cadastrar os produtos
    pyautogui.press("enter")

    # Rola a pagina pra cima
    pyautogui.press("pageUP")

