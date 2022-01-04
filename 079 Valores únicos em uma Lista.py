lista = []
lista.append(int(input(f'Digite o 1 valor da lista: ')))
print(f'O número {lista} foi adicionado!')
e = str(input('Quer continuar? [S/N]'))
while e.upper()[0] not in 'SN':
    e = str(input('Dados Inválidos. Quer continuar? [S/N]'))
c = 2
while e.upper()[0] == 'S':
    n = int(input(f'Digite o {c} valor da lista: '))
    if n not in lista:
        lista.append(n)
        print(f'O número {n} foi adicionado!')
    else:
        print('Número já existente!')
    e = str(input('Quer continuar? [S/N]'))
    while e.upper()[0] not in 'SN':
        e = str(input('Dados Inválidos. Quer continuar? [S/N]'))
lista.sort()
print('=-=' * 40)
print(f'Você digitou os valores {lista}')