import pyautogui
import time

# Se tiver disponivel, tenta realizar a compra
def verifica_ingresso():    
    pyautogui.click(x = 2500, y = 494)
    time.sleep(0.5)
    pyautogui.click(x = 2502, y = 608)

def compra_ingresso():
    pyautogui.click(x = 2533, y = 831)
    time.sleep(0.5)
    pyautogui.click(x = 2403, y = 697)
    time.sleep(0.5)
    pyautogui.click(x = 2004, y = 654)
    time.sleep(0.5)
    pyautogui.click(x = 2377, y = 745)
    time.sleep(3)
    pyautogui.click(x = 2148, y = 516)
    time.sleep(0.5)

def valida_cpf():
    pyautogui.doubleClick(x=2191, y= 279)
    pyautogui.write("49307549842")
    pyautogui.leftClick(x = 2431, y = 279)


# faz a verificação do ingresso
def main(): 
    valida_cpf()    
    time.sleep(2)
    pyautogui.scroll(-450)
    time.sleep(1)
    pyautogui.scroll(-450)
    time.sleep(1)

    x = 2478
    y = 455
    cor_desejada = (214, 17, 0)
    try:             
        while pyautogui.pixelMatchesColor(x, y, cor_desejada):
            pyautogui.scroll(450)
            pyautogui.scroll(450)
            
            valida_cpf()
            pyautogui.click(x=2425, y=275)
            time.sleep(2)
            pyautogui.scroll(-450)
            pyautogui.scroll(-450)

        # Clica no primeiro link dos resultados
            pyautogui.click(x=2425, y=275)
        # Espera a página abrir
            time.sleep(1)
        verifica_ingresso()
        compra_ingresso()
        #return main()
        pyautogui.PAUSE()
        
    except KeyboardInterrupt:
        pass

    print("\nPrograma Pausado")


    # Fecha o Google Chrome
    #pyautogui.hotkey('alt', 'f4')
main()