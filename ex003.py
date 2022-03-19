import operator

koto = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é ',type(koto))
print('Só tem espaços? ',koto.isspace())
print('É um número? ',koto.isnumeric())
print('É alfabético? ', koto.isalpha())
print('É alfanumérico? ', koto.isalnum())
print('Está em letras maiúsculas? ', koto.isupper())
print('Está em letras minusculas? ', koto.islower())
print('Está capitalizada? ', koto.istitle())
