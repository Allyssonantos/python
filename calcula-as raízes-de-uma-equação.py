from math import pow

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
Delta = b*b - 4*a*c
if Delta < 0:
    print("esta equação não possui raízes reais")
elif Delta == 0:
    raiz = (-b + pow(Delta,1/2))/2*a
    print("a raiz desta equação é", raiz)
else:
    print("Duas raízes")
    raiz1 = (-b + pow(Delta,1/2))/2*a
    raiz2 = (-b - pow(Delta,1/2))/2*a
    print("as raízes da equação são ", raiz1, "e", raiz2)

