x = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(x))
print('Só tem espaços? ', x.isspace())
print('Só tem números? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúsculas? ', x.islower())
print('Está em minúsculas? ', x.isupper())
print('Está capitalizada? ', x.istitle())