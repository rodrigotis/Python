# Desafio 019 = um professor quer sortear um dos seus alunos para
# apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido.
import random

a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ' )
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
a = [a1, a2, a3, a4]
print('A pessoa que apagará o quadro hoje será: {}!'.format(random.choice(a)))
