n = int(input('Digite um número [999 para parar]: '))
c = soma = 0
while True:
    if n == 999:
        break
    else:
        c += 1
        soma += n
    n = int(input('Digite um número [999 para parar]:'))
print(f'Foram digitados {c} números e a soma entre eles é igual a {soma}.')