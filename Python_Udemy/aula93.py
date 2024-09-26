# type: ignore
# Try, except, else e finally
#a = 18
#b = 0
#c = a / b    
try:
    a = 18
    b = 0
    print(b[0])
    print('Linha 1')
    c = a / b    
except ZeroDivisionError:
    print('Diviu por zero')
except NameError:
    print('Nome b não está definido')
except (Exception) as error:
    print('ERROR DESCONHECIDO', error.__class__.__name__)


print('CONTINUAR')
