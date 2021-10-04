# Desafio 015: Escreva um programa que pergunte a quantidade de
# Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

c = input('Qual o veículo está sendo devolvido? ')
km = float(input('Quantos quilometros foram percorridos? '))
d = int(input(f'Por quantos dias esteve com o {c}? '))
t = km * 0.15 + d * 60

print('-=' * 20)
print(f'Relatório de Locação\n'
      f'O carro \033[7;31;40m{c}\033[m foi alugado por \033[1;31m{d}\033[m dias\n'
      f'e percorreu \033[1;31m{km:.2f}\033[mKm.')

print('-=' * 20)
print('O valor por Km rodado é de \033[4mR$ 0,15\033[m.\n'
      'O valor por dia é de R$ \033[4m60,00\033[m')

print('-=' * 20)

print(f'Total pela locação = R$ \033[1;31;40m{t}\033[m!')

print('-=' * 20)