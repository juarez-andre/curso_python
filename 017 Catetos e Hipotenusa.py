from math import sqrt
x = float(input('Comprimento do cateto oposto: '))
y = float(input('Comprimento do cateto adjacente: '))
z = x ** 2 + y ** 2
print('A hipotenusa vai medir {:.2f}.'.format(sqrt(z)))
