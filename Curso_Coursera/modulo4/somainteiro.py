# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:27:30 2023

@author: efmiranda
"""

n = int(input("Digite um número inteiro: "))

soma = 0
while n > 0:
    digito = n % 10
    soma += digito
    n //= 10

print(soma)


