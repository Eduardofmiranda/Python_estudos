import random
for _ in range(100):
    nove_digitos = ''
    for k in range(9):
        nove_digitos += str(random.randint(0, 9))    
    i = 10
    total_digito_1 = 0
    # Iterar sobre cada dígito do CPF sem pontos e hífen
    for digito_1 in nove_digitos:
        total_digito_1 += int(digito_1) * i    
        i -= 1
    resto_1 = (total_digito_1 * 10)% 11
    resto_1 = resto_1 if resto_1 <= 9 else 0

    dez_digitos = nove_digitos + str(resto_1)
    total_digito_2 = 0
    j = 11
    for digito_2 in dez_digitos:
        total_digito_2 += int(digito_2) * j
        j -= 1
    resto_2 = (total_digito_2 * 10) % 11
    resto_2 = resto_2 if resto_2 <= 9 else 0
    cpf_gerado_pelo_calculo = f'{nove_digitos}{resto_1}{resto_2}'

    print(cpf_gerado_pelo_calculo)