lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um valor para a lista: '))
    if n % 2 == 0:
        listap.append(n)
        lista.append(n)
    else:
        listai.append(n)
        lista.append(n)
    e = str(input('Quer continuar? [S/N]'))
    if e[0] in 'Nn':
        break
print(f'A lista original é: {lista}')
print(f'A lista de números ímpares é: {listai}')
print(f'A lista de números pares é: {listap}')