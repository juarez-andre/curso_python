x = int(input('Digite um número para ver seu valor em binário: '))
print(f'O valor {x} convertido para binário é igual a: ', end='')
lista = []
while True:
    if x >= 2:
        c = x % 2
        if c > 0:
            lista.append(c)
        else:
            lista.append(c)
    else:
        lista.append(x)
        break
    x = x // 2
y = len(lista) - 1
while True:
    print(lista[y], end='')
    y -= 1
    if y < 0:
        break
