"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import sys

#cpf_enviado_usuario = '493.075.498-42'\
#    .replace('.','')\
#    .replace(' ','')\
#    .replace('-','')
entrada = input('CPF [493-075-498-42]: ')
cpf_enviado_usuario = re.sub(r'[^0-9]',
                             '',     
                             entrada                        
)
entrada_e_repetida = entrada == entrada[0] * len(entrada)
if entrada_e_repetida:
    print('CPF SENQUENCIAL')
    sys.exit()
nove_digitos = cpf_enviado_usuario[:9]
dez_digitos = cpf_enviado_usuario[:10]
j = 11
i = 10
total_digito_1 = 0
total_digito_2 = 0
# Iterar sobre cada dígito do CPF sem pontos e hífen
for digito_1 in nove_digitos:
    total_digito_1 += int(digito_1) * i    
    i -= 1
resto_1 = (total_digito_1 * 10)% 11
resto_1 = resto_1 if resto_1 <= 9 else 0
for digito_2 in dez_digitos:
    total_digito_2 += int(digito_2) * j
    j -= 1
resto_2 = (total_digito_2 * 10) % 11
resto_2 = resto_2 if resto_2 <= 9 else 0
cpf_gerado_pelo_calculo = f'{nove_digitos}{resto_1}{resto_2}'
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é valido')
else:
    print('cpf invalido')

