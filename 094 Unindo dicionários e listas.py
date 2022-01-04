dicio = dict()
lista = []
quantidade = 0
soma = 0
listamulher = list()
listavelho = list()
listavelhon = list()
listavelhos = list()
while True:
    dicio["Nome"] = str(input('Nome: '))
    dicio["Sexo"] = str(input('Sexo [M/F] '))
    while dicio["Sexo"][0] not in 'MmFf':
        dicio["Sexo"] = str(input('Dado Inválido. Sexo: [M/F] '))
    if dicio["Sexo"][0] in 'Ff':
        listamulher.append(dicio["Nome"])
    dicio["Idade"] = int(input('Idade: '))
    listavelhon.append(dicio["Nome"])
    listavelhos.append(dicio["Sexo"])
    listavelho.append(dicio["Idade"])
    soma += dicio["Idade"]
    lista.append(dicio.copy())
    quantidade += 1
    dicio.clear()
    e = str(input('Quer continuar? [S/N] '))
    while e[0] not in 'SsNn':
        e = str(input('ERRO! Quer continuar? [S/N] '))
    if e[0] in 'Nn':
        break
print('=-' * 30)
print(f'Ao todo temos {quantidade} pessoa(s) cadastradas.')
print(f'A média de idade do grupo é de {(soma / quantidade):.2f} anos.')
print(f'As mulheres cadastradas foram: {listamulher}.')
print('=-' * 30)
print('Pessoas com idade acima da média:')
for i, v in enumerate(listavelho):
    if listavelho[i] > soma / quantidade:
        print(f'Nome = {listavelhon[i]}; Sexo = {listavelhos[i]}; Idade = {listavelho[i]}')
print('=-' * 30)