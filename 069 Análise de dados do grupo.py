ci = 0
ch = 0
cm = 0
i = int(input('Qual a idade? '))
s = str(input('Qual o sexo? [M/F] ')).strip()
while s.upper() != 'M' and s.upper() != 'F':
    s = str(input('Qual o sexo? [M/F] ')).strip()
cont = str(input('Quer continuar? [S/N]')).strip()
while cont.upper() != 'S' and cont.upper() != 'N':
    cont = str(input('Quer continuar? [S/N]')).strip()
if i > 18:
    ci += 1
if s.upper() == 'M':
    ch += 1
if s.upper() == 'F' and i < 20:
    cm += 1
while cont.upper() == 'S':
    i = int(input('Qual a idade? '))
    s = str(input('Qual o sexo? [M/F] ')).strip()
    while s.upper() != 'M' and s.upper() != 'F':
        s = str(input('Qual o sexo? [M/F] ')).strip()

    if i > 18:
        ci += 1
    if s.upper() == 'M':
        ch += 1
    if s.upper() == 'F' and i < 20:
        cm += 1
    cont = str(input('Quer continuar? [S/N]')).strip()
    while cont.upper() != 'S' and cont.upper() != 'N':
        cont = str(input('Quer continuar? [S/N]')).strip()
print(f'No total, {ci} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {ch} homens.')
print(f'No total, {cm} mulheres tem menos de 20 anos.')
