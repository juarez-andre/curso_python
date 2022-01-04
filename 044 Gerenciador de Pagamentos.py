p = float(input('Preço do produto: '))
print('[ 1 ] à vista no dinheiro ou cheque.')
print('[ 2 ] à vista no cartão.')
print('[ 3 ] em até 2x no cartão.')
print('[ 4 ] em 3x ou mais no cartão.')
c = int(input('Selecione o número da opção: '))
avd = p - ((p * 10) / 100)
avc = p - ((p * 5) / 100)
p2x = p
p3x = p + ((p * 20) / 100)
while c != 1 and c != 2 and c != 3 and c != 4:
    print('Número Inválido. Tente novamente.')
    c = int(input('Selecione o número da opção: '))
if c == 1:
    print('O valor a pagar é de R${:.2f}.'.format(avd))
elif c == 2:
    print('O valor a pagar é de R${:.2f}.'.format(avc))
elif c == 3:
    print('O valor a pagar é de R${:.2f}.'.format(p2x))
elif c == 4:
    print('O valor a pagar é de R${:.2f}.'.format(p3x))
