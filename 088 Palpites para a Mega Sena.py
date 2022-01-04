from random import randint
lista = []
secundaria = []
q = int(input('Quantos jogos serão? '))
for c in range(1, q + 1):
    for p in range(1, 7):
        secundaria.append(randint(1, 60))
    lista.append(secundaria[:])
    secundaria.clear()
print('-=' * 19)
x = 1
for c in lista:
    print(f'Jogo {x}:', end=' ')
    for p in c:
        print(f'[{p:^2}]', end=' ')
    print()
    x += 1
    print('-=' * 19)