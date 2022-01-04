from time import sleep
import random
print('-=-' * 20)
print('PEDRA, PAPEL E TESOURA')
print('-=-' * 20)
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
e = int(input('Qual você escolhe? '))
pc = random.randint(1, 3)
while e != 1 and e != 2 and e != 3:
    print('Número Inválido. Tente novamente.')
    e = int(input('Qual você escolhe? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 20)
if pc == 1:
    print('Eu escolho PEDRA.')
elif pc == 2:
        print('Eu escolho PAPEL.')
else:
    print('Eu escolho TESOURA.')
if e == 1:
    if pc == 1:
        print('EMPATOU.')
    elif pc == 2:
        print('EU GANHEI.')
    else:
        print('VOCÊ GANHOU.')
elif e == 2:
    if pc == 1:
        print('VOCÊ GANHOU.')
    elif pc == 2:
        print('EMPATOU.')
    else:
        print('EU GANHEI.')
elif e == 3:
    if pc == 1:
        print('EU GANHEI.')
    elif pc == 2:
        print('VOCÊ GANHOU.')
    else:
        print('EMPATOU.')
print('-=-' * 20)

