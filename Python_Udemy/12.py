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
        
    
if __name__ == '__main__': 
    n, m = int(input().split())
    create_door_mat(n, m)