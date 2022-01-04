n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m >= 7:
    print('APROVADO.')
elif m >= 5 and m <= 6.9:
    print('RECUPERAÇÃO.')
else:
    print('REPROVADO.')