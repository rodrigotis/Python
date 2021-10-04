# Exercício 017
# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo e calcule e mostre
# o comprimento da hipotenusa

import math
c1 = float(input('Digite a medida do cateto adjacente:' ))
c2 = float(input('Digite, agora a medida do cateto oposto: '))
# o método hypot da biblioteca math calcula automaticamente a hipotenusa
# ao informar as medidas dos catetos.
h = math.hypot(c1,c2)
print('O cateto adjacente tem {:.2f}, o cateto oposto tem {:.2f}'
      ' e a hipotenusa é {:.2f}'.format(c1, c2, h))