from random import randint
def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(1, 6):
        x = randint(1, 10)
        lista.append(x)
        print(x, end=' ')
    print('PRONTO!')


def sorteiapar(lista):
    soma = 0
    for i, v in enumerate(lista):
        if v % 2 == 0:
            soma += v
    print(f'A soma dos números pares presentes na lista {numeros} é igual a {soma}.')
numeros = []
sorteia(numeros)
sorteiapar(numeros)
