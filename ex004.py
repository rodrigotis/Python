# DESAFIO 3: faça um programa que leia algo pelo teclado
# e mostre na tela seu tipo primitivo e todas as informações sobre ela

n = input("Digite algo aqui: ")
print('O que você digitou é um dado do tipo ', type(n))
print('É um dado alfanumérico? = ', n.isalnum())
print('É um dado alfabético? = ', n.isalpha())
print('É um dado somente com letras minúsculas? = ', n.islower())
print('É um dado numérico? = ', n.isnumeric())
print('É um dado somente de espaços? = ', n.isspace())
print('É um dado somente com letras maiúsculas? = ', n.isupper())

