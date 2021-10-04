# Desafio 034 = Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento.

# Para salários superiores a R$ 1250.00, calcule um aumento de 10%
# Para salários inferiores ou iguais, o aumento é de 15%.

s = float(input('Olá, qual é seu salário atual? R$ '))

if s <= 1250.00:
    sn = s * 0.15 + s
else:
    sn = s * 0.1 + s

print(f' O novo salário é de R$ {sn:.2f}')