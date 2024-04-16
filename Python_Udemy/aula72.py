
def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_ou_impar(numero):
    return numero % 2 == 0
    

par = par_ou_impar(2)
print(par)


#multiplica1 = multiplica(1,2,3,4,5)
#print(multiplica1)