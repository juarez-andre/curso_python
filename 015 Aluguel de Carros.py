x = float(input('Km percorridos: '))
y = int(input('Quantidade de dias que foi alugado:'))
p = (x * 0.15) + (y * 60)
print('O total a pagar é R${:.2f}.'.format(p))