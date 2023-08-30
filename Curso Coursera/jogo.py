import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))


delta = b**2 - 4 * a * c

class Conta:
    def _init_(self,a,b,c,delta):
        self.a = a
        self.b = b
        self.c = c
        sesf.d = delta

    def raiz1(self):
        return (-b + math.sqrt(delta)) / (2 * a)

    def raiz2(self):
        return (-b - math.sqrt(delta)) / (2* a)

c = Conta()

if delta == 0:    
    print("A única raiz é: ", c.raiz1())
else:
    if delta < 0:
        print("Esta equação não possui raízes reais")
    else:
        print(c.raiz1())
        print(c.raiz2())
    




