# desafio 012 = faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço com 5% de desconto

n = input(('Qual o nome do produto? '))
po = float(input('Qual é seu preço? R$ ')) #po = preço original
d = 0.05
pn = po - 0.05 * po #pn = preço novo
print(f'Hoje, o produto \033[1;34;40m{n}\033[m está em promoção!\n'
      f'Somente hoje por R$ \033[4;35m{pn:.2f}\033[m! Aproveite!')