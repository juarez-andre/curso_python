soma = 0
n = int(input('Digite um número: '))
cont = str(input('Quer continuar? '))
soma += n
c = 1
maior = n
menor = n
while cont.upper() == 'S':
    n = int(input('Digite um número: '))
    cont = str(input('Quer continuar? '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    c += 1
print('A média entre os números digitados é {}.'.format(soma / c))
print('O maior número digitado foi {} e o menor número digitado foi {}.'.format(maior, menor))
