# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:20:27 2023

@author: efmiranda
"""

def maior_primo(n):
    for num in range(n, 1, -1):
        if is_primo(num):
            return num

def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True