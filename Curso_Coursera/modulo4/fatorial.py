# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:43:56 2023

@author: efmiranda
"""

n = int(input("Digite o valor de n: "))
fatorial = 1
i = 1

while i <= n:
    fatorial *= i
    i += 1
print(fatorial)