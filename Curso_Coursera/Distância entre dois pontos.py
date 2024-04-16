x1 = int(input("Informe o valor 1: "))
x2 = int(input("Informe o valor 2: "))
y1 = int(input("Informe o valor 3: "))
y2 = int(input("Informe o valor 4: "))


conta = ((x1 - y2) ** 2) + ((x2 - y2) ** 2)

if conta >= 10:
    print("longe")
else:
    print("perto")
