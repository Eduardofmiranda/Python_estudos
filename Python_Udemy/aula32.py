"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um numero inteiro: ')
if numero_str.isdigit():
    entrada_int = int(numero_str)
    par_impar = entrada_int % 2== 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario_str = input('Digite o horario: ')
horario_int = int(horario_str)
bom_dia = horario_int >= 0 and horario_int <= 11
boa_tarde = horario_int >= 12 and horario_int <= 17
boa_noite = horario_int >= 18 and horario_int <= 23
if bom_dia:
    print('Bom dia')
if boa_tarde:
    print('Boa tarde')
if boa_noite:
    print('Boa noite')

"""
"""

nome = input('Digite seu nome: ')
tamanho_do_nome = len(nome)
try:
    if tamanho_do_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_do_nome <= 5 or tamanho_do_nome <= 6:
        print('Seu nome é normal')
    elif tamanho_do_nome > 6:
        print('Seu nome é muito grande')
    else:
        print('Entrada invalida')
except ValueError:
    print('Entrada invalida')