#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalEfficiency' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY skill as parameter.
#

def getTotalEfficiency(skill):
    skill.sort()  # Ordena as habilidades em ordem crescente
    n = len(skill)
    
    total_efficiency = 0
    
    for i in range(n // 2):
        total_efficiency += skill[i] * skill[n - i - 1]
    
    return total_efficiency

# Exemplo de entrada
skill = [3, 4]

# Chama a função e imprime o resultado
print(getTotalEfficiency(skill))

