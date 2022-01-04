def leiaInt(nome):
    print('Você acabou de digitar o número {}.'.format(nome))


n = str(input('Digite um número: '))
while True:
    if n.isnumeric():
        while True:
            if float(n) % 1 != 0:
                print('\033[31mERRO! Digite um número inteiro válido: \033[m')
                n = str(input('Digite um número: '))
            else:
                break
        leiaInt(n)
        break
    else:
        print('\033[31mERRO! Digite um número inteiro válido: \033[m')
        n = str(input('Digite um número:'))

