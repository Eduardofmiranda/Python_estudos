# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:01:18 2023

@author: efmiranda
"""
decrescente = True
anterior = int(input("Digite o primeiro numero da sequencia: "))

valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o proximo numero da sequencia: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print("A sequencia está em ordem decrescente!")
    
else:
    print("A sequencia não está em ordem decrscente!")
        