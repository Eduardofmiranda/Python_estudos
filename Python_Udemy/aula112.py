# map - para mapear dados
import copy
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]

novos_produtos = filter(
    lambda p: p['preco'] > 10,
    produtos
)
def ordena_por_nome(produto):
    return list(sorted(produto, key=lambda p:p['nome']))
def ordena_por_preco(produto):
    return list(sorted(produto, key=lambda p:p['preco']))



# print_iter(produtos)
# print_iter(novos_produtos)
print_iter(ordena_por_nome(filter(lambda p:p['preco'] > 1, produtos)))
print_iter(ordena_por_preco(filter(lambda p:p['preco'] > 10, produtos)))

