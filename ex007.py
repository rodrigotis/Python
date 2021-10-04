# Desafio 007 = desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre sua média

n = input('Qual é o nome do(a) aluno(a)?')
n1 = float(input('Qual foi a nota na primeira prova de  Matemática? '))
n2 = float(input('Qual foi a nota na segunda prova de  Matemática? '))
m = (n1 + n2) / 2 # a ordem de procedência foi alterada porque n1 e n2 foram postos em ()

print(f'Relatório Bimestral\nO(a) aluno(a) {n} obteve as seguintes notas:\n'
      f'{n1} na primeira prova de Matemática\n'
      f'{n2} na segunda prova.\n'
      f'Obteve a média {m:.1f}')