# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:57:21 2023

@author: efmiranda
"""

numero = int(input("Digite um número inteiro positivo: "))

if numero > 1:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print("não primo")
            break
    else:
        print("primo")
else:
    print("não primo")
