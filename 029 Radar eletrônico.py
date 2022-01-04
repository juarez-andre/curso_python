v = float(input('Qual a velocidade do veículo? '))
m = (v - 80) * 7
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia! Dirija com segurança!')