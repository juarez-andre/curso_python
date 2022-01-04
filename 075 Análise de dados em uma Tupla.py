w = int(input())
x = int(input())
y = int(input())
z = int(input())
tupla = (w, x, y, z)
print(tupla.count(9))
if 3 in tupla:
    print(tupla.index(3))
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os números pares foram:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')