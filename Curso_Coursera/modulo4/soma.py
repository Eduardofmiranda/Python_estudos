# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:55:58 2023

@author: efmiranda
"""
print("Digite uma sequencia de valores terminada por zero.")

soma = 0 
valor = 1


while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor

print("A soma dos valores digitados é: ", soma)

