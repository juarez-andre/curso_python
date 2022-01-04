n = c = soma = 0
n = int(input('Digite um número: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número: '))
print('Foram digitados um total de {} números.'.format(c))
print('A soma de todos os números digitados foi de {}.'.format(soma))