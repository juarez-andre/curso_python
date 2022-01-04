m = 0
co = 0
c = 0
velho = 0
novas = ''
arem = ''
for c in range(1, 5):
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo: '))
    c += 1
    co += i
    if s == 'masculino':
        if c == 1:
            velho =+ i
            nv = n
        else:
            if i > velho:
                velho = i
                nv = n
    else:
        if i < 20:
            novas = n
            arem = novas.join(' ')

m = co / 4
print('A média de idade do grupo é de {} anos.'.format(m))
print('O homem mais velho tem {} anos.'.format(velho))
print('As mulheres de menos de 20 anos são: {}.'.format(arem))





