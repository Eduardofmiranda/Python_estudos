# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:47:37 2023

@author: efmiranda
"""

def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fatorial(n-1)
    
    
def coeficiente_binomial(n, k):
    if k > n:
        return 0
    else:
        return fatorial(n) // (fatorial(k) * fatorial (n-k))
    
def main():
    n = int(input("Digite o valor de n: "))
    k = int(input("Digite o valor de k: "))
    
    coeficiente = coeficiente_binomial(n, k)
    
    print(f"O coeficiente binomial de ({n}, {k}) é: {coeficiente}")
main()
