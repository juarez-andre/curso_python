from datetime import datetime
dic = {"Nome": str(input('Nome: ')), "Nasc": int(input('Ano de Nascimento: ')), "CTPS": int(input('Carteira de Trabalho (0 não tem)? '))}
if dic["CTPS"] != 0:
    dic["Contratação"] = int(input('Ano de Contratação: '))
    dic["Salário"] = float(input('Salário: '))
print('=-' * 30)
for k, v in dic.items():
    if k == "Nome":
        print(f'{k} tem o valor {v}.')
    elif k == "Nasc":
        print(f'Idade tem o valor {datetime.now().year - v}')
    elif k == "CTPS":
        print(f'{k} tem o valor {v}')
    elif dic["CTPS"] != 0:
        if k == "Contratação":
            print(f'{k} tem o valor {v}')
        elif k == "Salário":
            print(f'{k} tem o valor R${v:.2f}')
apos = dic["Contratação"] - dic["Nasc"] + 35
print(f'Aposentadoria tem o valor {apos}.')
print('=-' * 30)
