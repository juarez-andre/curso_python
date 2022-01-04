pt = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
decimo = pt + (10 - 1) * r
x = pt
while x <= decimo:
    print(x, end=' - ')
    x += r
print('ACABOU')