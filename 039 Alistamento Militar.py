from datetime import date
a = int(input('Em que ano você nasceu? '))
if date.today().year - a > 18:
    print('Já passou {} anos do tempo de se alistar!'.format((date.today().year - a) - 18))
    print('Seu alistamento foi em {}.'.format(a + 18))
elif date.today().year - a == 18:
    print('Já está na hora de se alistar!')
else:
    print('Daqui {} anos você ainda terá que se alistar!'.format(18 - (date.today().year - a)))
    print('Seu alistamento será em {}.'.format(a + 18))

