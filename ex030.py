# Desafio 030 = Crie um programa que leia um número inteiro e mostre na tela se
# ele é PAR ou IMPAR

#Crie um programa que leia um número inteiro
num = int(input('Digite um número qualquer: '))
conta = num % 2
if conta == 0:
    print(f'O número escolhido foi {num}\n'
          f'Ele é um número par!')
else:
    print(f'O número escolhido foi {num}\n'
          f'Ele é um número impar!')