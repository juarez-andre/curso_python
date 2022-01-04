import math
x = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(x))
c = math.cos(math.radians(x))
t = math.tan(math.radians(x))
print('O ângulo de {} tem o seno de {:.2f}.'.format(x, s))
print('O ângulo de {} tem o cosseno de {:.2f}.'.format(x, c))
print('O ângulo de {} tem a tangente de {:.2f}.'.format(x, t))