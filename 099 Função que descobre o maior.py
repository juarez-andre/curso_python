def j(x, maior):
    print(f'O maior número digitado até agora foi: {mai}.')


mai = 0
c = 0
while True:
    y = int(input('Digite um número: '))
    if c == 0:
        mai = y
    if c != 0:
        if y > mai:
            mai = y
    j(y, mai)
    c += 1
    e = str(input('Quer continuar? [S/N] ')).upper()[0]
    while True:
        if e not in 'SN':
            e = str(input('Resposta inválida! Quer continuar? [S/N] ')).upper()[0]
        else:
            break
    if e in 'N':
        break
print(f'O maior número digitado foi: {mai}')
print('>>PROGRAMA ENCERRADO<<')