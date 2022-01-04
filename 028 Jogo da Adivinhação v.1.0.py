import random
import time
pc = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5... Tente adivinhar!')
print('-=-' * 20)
escolha = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(3)
print('Eu pensei no número {}.'.format(pc))
if escolha == pc:
    print('ACERTOU!!!')
else:
    print('ERROU!!!')