def ficha(n='<desconhecido>', g=0):
        print('O jogador {} fez {} gol(s) no campeonato.'.format(n, g))


nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
