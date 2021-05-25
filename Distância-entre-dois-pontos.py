x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

if x1 < 0 and x2 >= 0:  # cálculos para verificar a distância entre pontos do eixo x;
    x3 = (x1*-1) + x2
elif x1 >= 0 and x2 < 0:
    x3 = x1 + (x2 * -1)
elif x1 < 0 and x2 < 0:
    if x1 > x2:
        x3 = x1 - x2
    else:
        x3 = x2 - x1
elif x1 >= 0 and x2 >= 0:
    if x1 >= x2:
        x3 = x1 - x2
    else:
        x3 = x2 - x1
        
    
if y1 < 0 and y2 >= 0:  # cálculos para verificar a distância entre pontos no eixo y;
    y3 = (y1*-1) + y2
elif y1 >= 0 and y2 < 0:
    y3 = y1 + (y2 * -1)
elif y1 < 0 and y2 < 0:
    if y1 > y2:
        y3 = y1 - y2
    else:
        y3 = y2 - y1
elif y1 >= 0 and y2 >= 0:
    if y1 >= y2:
        y3 = y1 - y2    
    else:
        y3 = y2 - y1


import math
resultado = math.sqrt(x3**2 + y3**2) # Teorema de pitágoras para encontrar a distância mais curta entre os dois pontos do plano (hipótenusa);

if resultado >= 10:
    print("longe")
else:
    print("perto")