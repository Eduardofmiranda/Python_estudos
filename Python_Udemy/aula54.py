"""
Faça uma lista de compras com listas 
O usuário deve ter a opssibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de índices inexistentes na lista.
"""
import os
lista = []
while True:       
        print('Seleciona uma opção')
        opcao = input('[i]nserir [a]pagar [l]istar: ')        
        try:            
            if opcao == 'i':
                os.system('cls')
                valor = input('Valor: ')
                lista.append(valor)                
            elif opcao == 'a':
                indice_str = input('Escolha o índice para apagar: ')
                indice = int(indice_str)
                lista.pop(indice)            
                os.system('cls')                 
            elif opcao == 'l':
                os.system('cls')                
                for i, valor in enumerate(lista):
                    print(i, valor)         
        except ValueError:
             print('Digite um indice valido')
        except IndexError:
            print('Indice nao existe na lista')
        except:
            print('Erro desconhecido')                  
            if len(lista) == 0:
                print('Lista Vazia')                            
        else:
             print('Por favor, escolha i, a ou l.')
             

   



