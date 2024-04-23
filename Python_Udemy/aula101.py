def soma(x,y):
    return x + y

def multiplica(x,y):
    return x * y

def criar_funcao(funcao, x):    
    def adiada(y):
        return funcao(x,y)
    return adiada

soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco)
# multiplica_por_dex = criar_funcao(multiplica, 10)
