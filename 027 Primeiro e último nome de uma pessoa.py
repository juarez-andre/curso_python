x = str(input('Digite seu nome completo: ')).strip()
s = x.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(s[0]))
print('Seu último nome é {}.'.format(s[len(s) - 1]))


