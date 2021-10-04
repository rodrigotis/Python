# Desafio 033 = faça um programa que leia três números e mostre qual é o maior e qual é
# o menor

n = float(input('Digite um número qualquer: '))
n1 = float(input('Agora, digite mais um número: '))
n2 = float(input('Agora, o último: '))

t1 = n > n1, n > n2
t2 = n1 > n, n1 > n2
t3 = n2 > n, n2 > n1

print(f'Ótimo, você escolheu os números {n}, {n1} e `{n2}\n'
      f'Agora, qual deles é o maior? e o menor?')
if t1 == (True, True):
    print(f'{n} é maior')
elif t1 == (False, False):
    print(f'{n} é menor')

if t2 == (True, True):
    print(f'{n1} é maior')
elif t2 == (False, False):
    print(f'{n1} é menor')

if t3 == (True, True):
    print(f'{n2} é maior')
elif t3 == (False, False):
    print(f'{n2} é menor')