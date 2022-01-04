n = int(input('Digite um número para ver sua tabuada (valor negativo para parar): '))
while True:
    while n >= 0:
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
        n = int(input('Digite um número para ver sua tabuada (valor negativo para parar): '))
    else:
        break
