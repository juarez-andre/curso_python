x = str(input('Digite seu nome completo: ')).strip()
separa = x.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(x.upper()))
print('Seu nome em minúsculas é {}.'.format(x.lower()))
print('Seu nome completo tem {} letras.'.format(len(x) - x.count(' ')))
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))
print('Seu segundo nome é {} e tem {} letras.'.format(separa[1], len(separa[1])))