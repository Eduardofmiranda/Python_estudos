# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:46:43 2023

@author: efmiranda
"""

x1 = int(input("Digite o primeiro numero: "))
y1 = int(input("Digite o segundo numero: "))
x2 = int(input("Digite o terceiro numero: "))
y2 = int(input("Digite o quarto numero: "))

distancia = (((x1 - x2)** 2 + (y1 + y2)** 2)** 0.5)
if distancia >= 10:
    print("longe")
else:
    print("perto")