# escreva um programa que leia um valor em metros e o exiba convertido em
#centímetros e milímetros

n = float(input('Qual é a distância, em metros, do ponto A ao ponto B? '))
c = n*100
m = n*1000

print(f'A distância é de {n} metros,\n'
      f'ou {c} centímetros ou'
      f'\nincríveis {m} milímetros!')