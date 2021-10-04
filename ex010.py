# desafio 010 = crie um programa que leia quanto dinheiro uma pessoa tem
#na carteira e mostre quantos dólares ela pode comprar

c = float(input('Quantos Reais você tem no bolso agora? R$ '))
d = 3.27
d1 = c/3.27

print(f'Com R${c:.2f} você consegue comprar US${d1:.2f}')