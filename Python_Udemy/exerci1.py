# """
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# """

# entrada = input('Digite um numero: ')

# if entrada.isdigit():
#     entrada_int = int(entrada) 
#     par_impar = entrada_int % 2==0
#     par_impar_text = 'impar'
    
#     if par_impar:
#         par_impar_text = 'par'
    
#     print(f'O número {entrada_int} é {par_impar_text}')
# else:
#     print('Você não digitou um número inteiro')

# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """
# hora = input('Digite uma hora: ')
# horario_int = int(hora)
# manha = horario_int >= 0 and horario_int<= 11
# tarde = horario_int >= 12 and horario_int <= 17
# noite = horario_int >= 18 and horario_int<= 23

# if manha:
#     print('bom dia')
# if tarde:
#     print('boa tarde')
# if noite:
#     print('boa noite')

# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
# """

# nome = str(input('Digite seu nome: '))
# try:
#     if len(nome) <= 4:
#         print('Seu nome é muito curto')
#     if len(nome) >= 5 or len(nome) <= 6:
#         print('Seu nome é normal')
#     if len(nome) <= 6:
#         print('Seu nome é muito grande')
# except ValueError:
#     print('Entrada invalida')

