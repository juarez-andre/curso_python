n = int(input('Digite um número: '))
co = 0
for c in range(1, 12):
    print('{} x {} = {}'.format(n, co, (n * co)))
    co += 1
