# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:27:18 2023

@author: efmiranda
"""

def vogal(caractere):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if caractere.lower() in vogais:
        return True
    else:
        return False