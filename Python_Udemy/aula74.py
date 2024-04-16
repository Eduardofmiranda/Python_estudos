"""
Clousure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa Noite')

print(falar_bom_dia('Eduardo'))

for nome in ['Eduardo', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))