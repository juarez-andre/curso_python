matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor: '))
print(matriz)
soma = somat = mai = 0
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            somat += matriz[l][c]
        if l == 1:
            if c == 0:
                mai = matriz[l][c]
            else:
                if matriz[l][c] > mai:
                    mai = matriz[l][c]
    print()
print(f'A soma entre os valores pares da matriz é igual a {soma}.')
print(f'A soma entre os valores da terceira coluna é igual a {somat}.')
print(f'O maior valor da segunda linha é {mai}.')
print('=-' * 30)