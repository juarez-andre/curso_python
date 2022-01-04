s = float(input("Salário do funcionário: "))
if s <= 1250:
    nv = s + (s * 15) / 100
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, nv))
else:
    nv = s + (s * 10) / 100
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, nv))