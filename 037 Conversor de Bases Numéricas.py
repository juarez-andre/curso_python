n = int(input('Digite um número: '))
print('[ 1 ] converter para BINÁRIO.')
print('[ 2 ] converter para OCTAL.')
print('[ 3 ] converter para HEXADECIMAL')
e = int(input('Sua opção: '))
if e == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2::]))
elif e == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2::]))
elif e == 3:
    print('{} convertido para HEXADECIMAL é igual a  {}.'.format(n, hex(n)[2::]))
