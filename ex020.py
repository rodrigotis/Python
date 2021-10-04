# Desafio 020 = O mesmo professor quer sortear a ordem de apresentação dos alunos.
# Faça um programa que leia o nome dos quarto alunos e mostre a ordem sorteada.

import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
a = [a1, a2, a3, a4]
random.shuffle(a)
# o método shuffle embaralha e cria uma lista  para exibição do resultado
print(f'A ordem de apresentação será:\n'
      f'{a}')
