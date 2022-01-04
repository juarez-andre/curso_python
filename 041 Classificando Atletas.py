from datetime import date
a = int(input('Em que ano você nasceu? '))
i = date.today().year - a
if i <= 9:
    print('MIRIM.')
elif i <= 14 and i > 9:
    print('INFANTIL.')
elif i <= 19 and i > 14:
    print('JUNIOR.')
elif i >= 20 and i <= 25:
    print('SÊNIOR.')
else:
    print('MASTER.')