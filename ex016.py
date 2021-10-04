# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua
# porção inteira
## Exemplo: número digitado = 6.127
## na tela aparecerá apenas o inteiro: 6

from math import trunc
n = float(input("Digite um numero qualquer: "))
print(f'A parte inteira de {n} é {trunc(n)}. ')
