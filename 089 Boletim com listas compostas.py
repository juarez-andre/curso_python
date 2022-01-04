lista = list()
temp = []
while True:
    temp.append(str(input('Aluno(a): ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    lista.append(temp[:])
    temp.clear()
    e = str(input('Quer continuar continuar? [S/N]'))
    if e[0] in 'Nn':
        break
print('-=' * 40)
for c, p in enumerate(lista):
    print(f'A média do aluno(a) {p[0]} foi de {(p[1] + p[2]) / 2}')
a = str(input('Deseja ver as notas de qual aluno? (/ para interromper) '))
while a != '/':
    for c, p in enumerate(lista):
        if a.upper() == p[0].upper():
            print(f'As notas do aluno(a) {p[0]} foram [{p[1]}] e [{p[2]}]')
    a = str(input('Deseja ver a nota de qual aluno? (/ para interromper) '))