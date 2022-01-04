s = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while s != 'M' and s != 'F':
    print('Valor Incorreto. Tente novamente')
    s = str(input('Qual o seu sexo? [M/F] ')).upper()