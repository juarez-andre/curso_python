import math
x = float(input('Comprimento do cateto oposto: '))
y = float(input('Comprimento do cateto adjacente: '))
z = math.hypot(x, y)
print ('A hipotenusa vai medir {:.2f}.'.format(z))