# Desafio 026 = Faça um programa que leia a frase pelo teclado e mostre:
# a- Quantas vezes aparece a letra "A".
# b- Em que posição ela aparece a primeira vez
# c - Em que posição ela aparece a última vez

frase = input('Filosofe aqui: ').strip()
frase = frase.lower()
# a- Quantas vezes aparece a letra "A".
print('a', frase.count('a'))

# b- Em que posição ela aparece a primeira vez
print('b', frase.find('a')+1)

# c - Em que posição ela aparece a última vez
print('c', frase.rfind('a')+1)
