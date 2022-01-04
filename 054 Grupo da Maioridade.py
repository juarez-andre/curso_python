import datetime
cm = 0
cc = 0
for c in range(1, 8):
    x = int(input('Ano de nascimento: '))
    if datetime.date.today().year - x < 21:
        cc += 1
    else:
        cm += 1
print('Das 7 pessoas, {} são maiores de idade e {} ainda não são.'.format(cm, cc))