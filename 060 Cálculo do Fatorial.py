n = int(input('Digite um número para saber seu fatorial: '))
f = 1
for c in range(n, 0, -1):
    f *= c
print(f)
