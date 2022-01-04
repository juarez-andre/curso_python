pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
decimo = pt + (10 - 1) * r
x = pt
while x <= decimo:
    print(x, end=' - ')
    x += r
cont = int(input('Mostrar mais quantos termos? '))
if cont > 0:
    while cont > 0:
        for c in range (1, cont + 1):
            print(x, end=' - ')
            x += r
        cont = int(input('Mostrar mais quantos termos? '))