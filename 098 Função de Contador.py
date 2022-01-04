from time import sleep
def cont(i, f, p):
    print('=-' * 30)
    if f > i:
        if p < 0:
            p *= -1
        print(f'Contagem de {i} até {f} de {p} em {p}.')
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')
    elif i > f:
        if p > 0:
            print(f'Contagem de {i} até {f} de {p} em {p}.')
            p *= -1
        for c in range(i, f - 1, p):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')
    elif i == f:
        print('Valores iguais! Contagem inviável.')
cont(1, 10, 1)
cont(10, 0, 2)
print('=-' * 30)
print('Agora é sua vez de personalizar a contagem: ')
ii = int(input('Início: '))
ff = int(input('Fim: '))
pp = int(input('Passo: '))
if pp > 0:
    print(f'Contagem de {ii} até {ff} de {pp} em {pp}.')
else:
    print(f'Contagem de {ii} até {ff} de {pp * -1} em {pp * -1}.')
cont(ii, ff, pp)
