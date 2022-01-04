v = float(input('Valor da casa: '))
s = float(input('Salário do comprador: '))
a = float(input('Quantos anos para pagar? '))
p = v / (a * 12)
if p > (s * 30) / 100:
    print('EMPRÉSTIMO NEGADO.')
else:
    print('EMPRÉSTIMO ACEITO. A parcela mensal é de R${:.2f} ao longo de {:.0f} meses.'.format(p, a * 12))