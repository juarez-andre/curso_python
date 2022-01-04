lista = []
q = 0
g = 0
while True:
    lista.append(int(input('Digite um valor para a lista: ')))
    e = str(input('Quer continuar? [S/N]')).strip()
    while e.upper()[0] not in 'SN':
        e = str(input('Dado Inválido. Quer continuar?'))
    if e.upper()[0] in 'N':
        break
print(f'No total foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O número 5 está presente na lista.')
else:
    print('O número 5 NÃO está presente na lista.')
