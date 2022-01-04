n = int(input('Digite um número para saber seu fatorial: '))
f = n
fat = 1
while f <= n and f >= 1:
    fat *= f
    f -= 1
print('O fatorial de {} é igual a {}.'.format(n, fat))
