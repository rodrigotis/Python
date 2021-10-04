# Desafio 027 = faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o útimo nome separadamente.

#EX Ana Maria de Souza
#primeiro = Ana
#Último = Souza

nome = input('Digite seu nome completo: ').strip()

nome = nome.split()

print('Primeiro Nome:', nome[0])
print('Último Nome: ', nome[-1])
