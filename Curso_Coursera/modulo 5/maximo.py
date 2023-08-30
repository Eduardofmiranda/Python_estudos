# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 17:16:48 2023

@author: efmiranda
"""

def maximo(a, b, c):
    if a > b and a > c:
        return (a)
    elif b > a and b > c:
        return (b)
    else:
        return (c)
