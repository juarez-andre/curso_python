import random
co = 0
pc = random.randint(1, 10)
print('-=-' * 20)
print('Jogo de Advinhação v2.0')
print('-=-' * 20)
escolha = int(input('Em que número eu pensei? '))
while pc != escolha:
    co += 1
    print('Eu pensei em um número diferente de {}. Tente novamente.'.format(escolha))
    escolha = int(input('Em que número eu pensei? '))
print('Acertou! Você precisou de um total de {} tentativas.'.format(co + 1))