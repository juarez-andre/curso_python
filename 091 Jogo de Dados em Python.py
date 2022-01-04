from random import randint
from operator import itemgetter
from time import sleep
dic = {"jogador1": randint(1, 6),
       "jogador2": randint(1, 6),
       "jogador3": randint(1, 6),
       "jogador4": randint(1, 6)}
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
print('Valores sorteados:')
for k, v in dic.items():
    print(f'{k} tirou {v}')
    sleep(1)
print('=-' * 30)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
print('=-' * 30)