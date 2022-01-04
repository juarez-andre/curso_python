from time import sleep
while True:
    sleep(1)
    x = 'SISTEMA DE AJUDA pyHELP'
    print('\033[42m', end='')
    print('-' * (len(x) + 4))
    print(f'\033[42m  {x}')
    print('-' * (len(x) + 4))
    print('\033[m', end='')
    sleep(1)
    c = str(input('Função ou Biblioteca > '))
    if c.upper() == 'FIM':
        break
    y = f'Acessando o manual do comando "{c}"...'
    print('\033[44m', end='')
    print('-' * (len(y) + 4))
    print(f'  {y}')
    print('-' * (len(y) + 4))
    print('\033[m', end='')
    sleep(3)
    print('\033[43m', end='')
    help(c)
    print('\033[m', end='')
s = '>> PROGRAMA ENCERRADO<<'
print('\033[41m', end='')
print('-' * (len(s) + 4))
print(f'  {s}')
print('-' * (len(s) + 4))
print('\033[m')