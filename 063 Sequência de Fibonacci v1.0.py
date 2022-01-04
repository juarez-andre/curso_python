n = int(input('Quantos termos você quer mostrar? '))
c = 0
tx = 0
ty = 1
t = 0
print('0 - 1', end=' - ')
while c <= n - 3:
    t = tx + ty
    c += 1
    print(t, end=' - ')
    tx = ty
    ty = t
print('ACABOU')





