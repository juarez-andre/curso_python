principal = []
secundaria = []
mai = 0
men = 0
while True:
    secundaria.append(str(input('Nome: ')))
    secundaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        mai = men = secundaria[1]
    else:
        if secundaria[1] > mai:
            mai = secundaria[1]
        if secundaria[1] < men:
            men = secundaria[1]
    principal.append(secundaria[:])
    secundaria.clear()
    e = str(input('Deseja continuar? [S/N]'))
    if e[0] in 'Nn':
        break
print('-=-' * 40)
print(f'Foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso foi de {mai}. Peso de', end=' ')
for c in principal:
    if c[1] == mai:
        print(f'{c[0]}', end=' ')
print()
print(f'O menor peso foi de {men}. Peso de', end=' ')
for c in principal:
    if c[1] == men:
        print(f'{c[0]}', end=' ')