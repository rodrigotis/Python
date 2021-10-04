#Exercício 018 = faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse angulo.

import math
a = float(input('Digite um ângulo qualquer: '))
#os métodos sin, cos e tan por si só não mostram os devidos resultados.
#para aparecer os valores corretamente é necessário transformar os números
# em radianos, atravez do método radians
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))



print(f'O ângulo escolhido foi {a}º\n'
      f'O Seno deste ângulo é {s:.2f}\n'
      f'O Cosseno é {c:.2f}\n'
      f'A Tangente é {t:.2f}!')