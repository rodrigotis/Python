# Exercício 017
# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo e calcule e mostre
# o comprimento da hipotenusa

co = float(input('Qual é a medida do cateto oposto? '))
ca = float(input('Qual é a medida da cateto  adjacente? '))
hipo = (co**2+ca**2)**(1/2)

print(f'A hipotenusa deste triângulohipo é {hipo:.2f}')

