# Desafio 028 = Escreva um programa que faça o computador "pensar" em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

#o programa deverá escrever na tela se o usuário venceu ou perdeu.
# a) faça o computador "pensar" em um número inteiro entre 0 e 5
import random
# outra forma de randomizar os números é com o randint(randomiza números inteiros dentro do
# intervalor selecionado. EX: randint(0, 5)  - ele vai randomizar os números dentro dessa escolha.

n = (0, 1, 2, 3, 4, 5)
s = random.choice(n)
print(s)
# b) peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

print('O computador escolheu um número entre 0 a 5, consegue descobrir qual foi?')
a = int(input('Digite aqui sua aposta: '))

if a == s:
    print(f'Parabéns seu sortudo! O número escolhido foi {s}!')
else:
    print(f'Mais sorte na próxima, o número escolhido foi {s}!')