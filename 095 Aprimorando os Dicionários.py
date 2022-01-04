gols = list()
jogador = dict()
time = list()
while True:
    gols.clear()
    jogador.clear()
    jogador["nome"] = str(input('Nome do jogador: '))
    q = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, q + 1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador["gols"] = gols.copy()
    jogador["total"] = sum(gols)
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    time.append(jogador.copy())
    if cont == 'N':
        break
print('=-' * 25)
print(f'{"cod"}', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 25)
for i, v in enumerate(time):
    print(f' {i:<3}', end='')
    for c in v.values():
        print(f'{str(c):<15}', end='')
    print()
print('--' * 25)
while True:
    mostrar = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if mostrar == 999:
        break
    if mostrar >= len(time):
        print(f'ERRO! Não existe jogador com código {mostrar}.')
    print(f'-- LEVANTAMENTO DO JOGADOR {time[mostrar]["nome"]}:')
    for i, v in enumerate(time[mostrar]["gols"]):
        print(f'    No jogo {i} fez {v} gols.')


