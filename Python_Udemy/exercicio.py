import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


novos_produtos = copy.deepcopy(produtos)
ordena_produto_nome_crescente = sorted(produtos, key=lambda nome: nome['nome'])
ordena_produto_nome_decrescente = sorted(produtos, key=lambda nome: nome['nome'], reverse=True)

def teste():
    for nome in ordena_produto_nome_decrescente:
        print(nome['nome'])
    print('teste')

for nome in ordena_produto_nome_crescente:
    print(nome['nome'])
print()
for preco in produtos:
    aumenta_preco = preco['preco'] * 0.10
    preco['preco'] += aumenta_preco

for produto in produtos:
    print(f"{produto['nome']}, {produto['preco']:.2f}")


#print(novos_produtos)