print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 <= r2 + r3 and r2 <= r1 + r3 and r3 <= r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO.')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('O triângulo é ISÓCELES.')
    else:
        print('O triângulo é ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')