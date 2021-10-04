# Desafio 023 = faça um programa que leia um número qualquer
# de 0  a 9999 e mostre na tela cada um dos dígitos separados

#EX = número 1234
# unidade: 4
# dezena: 3
# centena: 2
# milhar: 1

num = int(input('Escolha um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'A unidade deste número é: {u}\n'
      f'A dezena deste número é: {d}\n'
      f'A centena deste número é: {c}\n'
      f'O milhar desse número é: {m}')