d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem de {:.1f}Km'.format(d))
if d <= 200:
    p = 0.5 * d
    print('E o preço da sua passagem será de R${:.2f}'.format(p))
else:
    p = 0.45 * d
    print('E o preço da sua passagem será de R${:.2f}.'.format(p))

