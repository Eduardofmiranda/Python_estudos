# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:18:16 2023

@author: efmiranda
"""

meuCartao = int(input("Digite o numero do seu cartão de credito: "))

cartaoLido = 1
encontreiMeuCartao = False

while cartaoLido != 0 and not encontreiMeuCartao:
    cartaoLido = int(input("Digite o numero do seu cartão de credito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartao = True
        
if encontreiMeuCartao:
    print("Meu cartao está la")
else:
    print("Meu cartao nao esta la")        



