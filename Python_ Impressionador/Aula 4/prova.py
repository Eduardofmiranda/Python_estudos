#O ano pode ser dividido igualmente por 4, é um ano bissexto, a menos que:
   # O ano pode ser dividido igualmente por 100, NÃO é um ano bissexto, a menos que:
       # O ano também é divisível por 400. Então é um ano bissexto.



def is_leap(year):
    leap = False
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))