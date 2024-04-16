# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 17:01:11 2023

@author: efmiranda
"""

def fizzbuzz(n):       
    if n % 3 == 0 and n % 5 == 0:
         return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return (n)



 