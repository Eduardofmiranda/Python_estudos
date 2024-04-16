

while True: 
    numero1_str = input("Digite o primeiro numero: ")
    numero2_str = input("Digite o segundo numero: ")
    operador = input("Digite qual operação deseja fazer (/ * - +): ")
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero1_str)
        num_2_float = float(numero2_str)
        numeros_validos = True        
    except Exception as e1:      
        numeros_validos = None

    operadores_permitidos = '+-*/'

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    if operador not in operadores_permitidos:
        print('Digite um operador válido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue         

    if operador == '/':
        print(f'{num_1_float} + {num_2_float}=' + num_1_float / num_2_float)        
    elif operador == '*':
        ### DIFERENTES FORMAS DE REALIZAR O PRINT
        calc = num_1_float * num_2_float
        print(calc)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=' + num_1_float - num_2_float)
        print(calc)
    elif operador == '+':
        calc = num_1_float + num_2_float
        print(calc)


    sair = input('Quer sair? [s]im: ').lower().startswith('s')    
    if sair is True:
        break