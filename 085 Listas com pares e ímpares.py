lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 == 0:
        lista[0].insert(0, valor)
    else:
        lista[1].append(valor)
print(f'Os valores pares digitados foram {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram {sorted(lista[1])}')