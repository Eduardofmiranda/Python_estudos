# if __name__ == '__main__':
#     n = int(input())
    
#     list = []
    
#     for _ in range(n):        
#         entrada = input().split()
#         if entrada[0] == 'insert':            
#             list.insert(int(entrada[1]), int(entrada[2])) # type: ignore
            
#         elif entrada[0] == 'remove':
#             list.remove(int(entrada[1]))
        
#         elif entrada[0] == 'append':
#             list.append(int(entrada[1]))
        
#         elif entrada[0] == 'sort':
#             list.sort()
        
#         elif entrada[0] == 'pop':
#             list.pop()
            
#         elif entrada[0] == 'reverse':
#             list.reverse()
            
#         elif entrada[0] == 'print':
#             print(list)      


def calc_hash_tuple(n):
    numeros = list(map(int, input().split()))[:n]
    tupla = tuple(numeros)
    hash_value = hash(tupla)
    print(hash_value)
    
# n = int(input())

# calc_hash_tuple(n)

# Only seems to work in Pypy:

# n = int(input()) 
# elements = tuple(map(int, input().split()))
# print(hash(elements))


#Replace all ______ with rjust, ljust or center. 

# thickness = 5 #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

import textwrap

# def wrap(string, max_width):
#     texto = textwrap.fill(string, max_width)    
#     return texto

#      i= 1
#     str_new = []
#     for str in string:
#         str_new.append(str)
#         if i % max_width == 0:
#             str_new.append('\n')
#         i +=1
#     return ''.join(str_new)

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

def create_door_mat(n, m):
    pattern = [('.|.' * (2*i + 1)).center(m, '-') for i in range(n//2)]
    
    for line in pattern:
        print(line)
        
    print('WELCOME'.center(m, '-'))
    
    for line in reversed(pattern):
        print(line)
        
def print_rangoli(tamanho):
    tamanho = [('-' )]
    
    
    

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product
from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT

def product(A, B):
    result = list(product(A, B))
    
    print(*result)
    


    
    
if __name__ == '__main__':
    # num_shoes = int(input())
    # shoe_sizes = list(map(int,input().split()))
    # num_customers = int(input())
    
    # inventory = Counter(shoe_sizes)
    
    # print(inventory)
    # total_money_earned = 0
    
    # for _ in range(num_customers):
    #     size, price = map(int,input().split())
        
    #     if inventory[size] > 0:
    #         total_money_earned += price
    #         inventory -= 1 
            
    
    # print(total_money_earned)
    
    # from collections import defaultdict
    # d = defaultdict(list)
    # d['python'].append("awesome")
    # d['something-else'].append("not relevant")
    # d['python'].append("language")
    # for i in d.items():
    #     print(i)
    
    # from collections import namedtuple

    # qtd_alunos = int(input())
    # columns = input().split()

    # Student = namedtuple('Student', columns)

    # total_marks = sum(int(Student(*input().split()).MARKS) for _ in range(qtd_alunos))

    # print(Student)

# from collections import OrderedDict

# ordinary_dictionary = OrderedDict()
# # ordinary_dictionary['a'] = 1
# # ordinary_dictionary['b'] = 2
# # ordinary_dictionary['c'] = 3
# # ordinary_dictionary['d'] = 4
# # ordinary_dictionary['e'] = 5

# # print(ordinary_dictionary)

# qtd_produtos = int(input())

# for _ in range(qtd_produtos):
#     entrada = input().rsplit(maxsplit=1)
#     name = entrada[0]
#     price = int(entrada[1])    
    
#     if name in ordinary_dictionary:
#         ordinary_dictionary[name] += price
#     else:
#         ordinary_dictionary[name] = price
    
# for name, price in ordinary_dictionary.items():
#     print(f'{name} {price}')


# from collections import OrderedDict

# ordinary_dictionary = OrderedDict()

# qtd_entradas = int(input())

# for _ in range(qtd_entradas):
#     word = input().strip()
    
#     if word in ordinary_dictionary:
#         ordinary_dictionary[word] += 1
#     else:
#         ordinary_dictionary[word] = 1
        
# print(len(ordinary_dictionary))

# print(' '.join(map(str, ordinary_dictionary.values())))

# from collections import OrderedDict

# ordinary_dictionary = OrderedDict()

# qtd_entradas = int(input())

# for _ in range(qtd_entradas):
#     word = input().strip()
    
#     if word in ordinary_dictionary:
#         ordinary_dictionary[word] += 1
#     else:
#         ordinary_dictionary[word] = 1
        
# print(len(ordinary_dictionary))

# print(' '.join(map(str, ordinary_dictionary.values())))

# dicionario = {'joao':25,
#               'maria': 30,
#               'Pedro': 22}
# nome = input("Digite um nome: ")

# if nome in dicionario:
#     print(f'a idade de {nome} é {dicionario[nome]} anos.')
# else:
#     print('nome não encontrado')


# from collections import Counter

# if __name__ == '__main__':
#     s = input()
    
#     counter = Counter(s)
    
#     sorted_characters = sorted(counter.items(), key=lambda x:(-x[1], x[0]))
    
#     for char, freq in sorted_characters[:3]:
#         print(char, freq)


# from itertools import permutations

# string = list('HACK')
# permuta = list(permutations(string, 2))

# for p in sorted(permuta):
#     print(''.join(p))


            