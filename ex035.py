# Desafio 035 = Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se eles podem ou não formar um triangulo.
## pesquisar sobre princípios de contrução de triangulos
### a condição de existência de um triângulo é que um de seus lados seja maior que a soma dois
# outros dois lados.

a = float(input('Escolha uma medida da reta "a": '))
b = float(input('Escolha a medida da reta "b": '))
c = float(input('Agora, escolha a medida da reta "c": '))

if a < b+c and b < a+c and c < a+b:
    print(f'Com as medidas {a}, {b} e {c} é possível contruir um triângulo!')
else:
    print(f'Com as medidas {a}, {b} e {c} não é possível construir triângulos')

