# Desafio 033 = faça um programa que leia três números e mostre qual é o maior e qual é
# o menor
## Outra resolução

n = int(input('Primeiro valor: '))
n1 = int(input('Segundo valor: '))
n2 = int(input('Terceiro valor: '))

#Verificando o menor
menor  = n #pré-definindo o menor valor em n
if n1<n and n1<n2:
    menor = n1
if n2<n and n2<n1:
    menor = n2
# note que a variável "menor" foi alterada dependendo dos resultados de if
#Verificando o maior

maior = n
if n2>n and n1>n2:
    maior = n1
if n2>n and n2>n1:
    maior = n2
print(f'O menor valor é {menor}, o maior valor é {maior}')
