dic = {"Jogador": str(input('Qual o nome do jogador? ')), "Partidas": int(input('Quantas partidas? '))}
x = []
contador = 0
for c in range(1, dic["Partidas"] + 1):
    x.append(int(input(f'Quantidade de gols na {c}° partida: ')))
    for i, v in enumerate(x):
        if i == len(x) - 1:
                contador += v
dic["Gols"] = x
dic["Total"] = contador
print('=--' * 30)
print(dic)
print('=--' * 30)
for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O total de gols feitos foi {contador}.')
for i, v in enumerate(x):
    print(f'=> Na partida {i + 1}, fez {v}.')