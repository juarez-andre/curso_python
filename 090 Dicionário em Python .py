d = dict()
d['nome'] = str(input('Nome: '))
d['media'] = float(input(f'Média de {d["nome"]}: '))
if d["media"] >= 7:
    d["situação"] = 'Aprovado(a)'
elif 5 <= d["media"] < 7:
    d["situação"] = 'Recuperação'
else:
    d["situação"] = 'Reprovado(a)'
print('=-' * 30)
for k, v in d.items():
    print(f'{k} é igual a {v}')
print('=-' * 30)