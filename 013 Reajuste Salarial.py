x = float(input('Qual o salário do funcionário?'))
y = x + (x * 15) / 100
print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(x, y))