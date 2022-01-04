from random import randint
pc =  randint(1, 3)
print('=-=' * 20)
print('PEDRA, PAPEL E TESOURA')
print('=-=' * 20)
print('''[1] PEDRA
[2] PAPEL
[3] TESOURA''')
escolha = int(input('Qual você escolhe? '))
cv = 0
while True:
    if escolha == 1 and pc == 1:
        print('Eu escolho PEDRA')
        print('EMPATE!')
    elif escolha == 1 and pc == 2:
        print('Eu escolho PAPEL')
        print('Eu venci!')
        break
    elif escolha == 1 and pc == 3:
        print('Eu escolho TESOURA')
        print('Você venceu!')
        cv += 1
    elif escolha == 2 and pc == 1:
        print('Eu escolho PEDRA')
        print('Você venceu!')
        cv += 1
    elif escolha == 2 and pc == 2:
        print('Eu escolho PAPEL')
        print('EMPATE!')
    elif escolha == 2 and pc == 3:
        print('Eu escolho TESOURA')
        print('Eu venci!')
        break
    elif escolha == 3 and pc == 1:
        print('Eu escolho PEDRA')
        print('Eu venci!')
        break
    elif escolha == 3 and pc == 2:
        print('Eu escolho PAPEL')
        print('Você venceu!')
        cv += 1
    elif escolha == 3 and pc == 3:
        print('Eu escolho TESOURA')
        print('EMPATE!')
    escolha = int(input('Qual você escolhe? '))
    pc = randint(1, 3)
print(f'Você me venceu por {cv} vezes consecutivas!')
