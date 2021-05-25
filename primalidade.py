x = int(input('Digite um número inteiro:'))
divisores = 0
for i in range(1, x):
    if x % i == 0:
        divisores += 1
if divisores >= 2:
    print('não primo')
else:
    print('primo')