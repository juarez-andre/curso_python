def fatorial(n, show=0):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    print('-' * 20)
    fat = 1
    for c in range(n, 0, -1):
        fat *= c
    if show:
        for c in range(n, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x', end=' ')
        print(fat)
    else:
        print(fat)
    print('-' * 20)


fatorial(10, show=False)
help(fatorial)