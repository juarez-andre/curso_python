tuplas = 'Pao', 'Carne', 'Macaco', 'Lontra', 'Marsupial', 'Taliba', 'Jacaré', 'Covid'
for c in tuplas:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')