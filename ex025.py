# Desafio 025 = crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input('Digite seu nome completo: ').strip()
nome = nome.upper()
print('SILVA' in nome)