# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 17:01:11 2023

@author: efmiranda
"""

def divisao(n):
    if n % 3 == 0 and n % 5 == 0:
         print("FizzBuzz")
    elif n % 3 == 0:
         print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    

def main():
    divisao(3)
    divisao(5)
    divisao(15)
    divisao(4)
main()
        
        