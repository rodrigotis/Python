# desafio 022 = crie um programa que leia o nome completo de uma pessoa e mostre:
# a- O nome com todas as letras maiúsculas
# b- o nome com todas as letras minúsculas
# c- quantas letras total ( sem considerar espaços)
# d- quantas letras tem o primeiro nome

nome = input('Escreva seu nome completo aqui: ')
# a- O nome com todas as letras maiúsculas
print('Seu nome com letras maiúsculas é assim: ', nome.upper())
# b- o nome com todas as letras minúsculas
print('Com todas minúsculas: ' , nome.lower())
# c- quantas letras total (sem considerar espaços)
print('Ele possui ', len(nome.replace(' ', '')), 'letras')
# também pode ser resolvido assim: len(nome) - nome.count(' ') _ ou seja, ele conta a qtd de espaços
# e tira do len.

# d- quantas letras tem o primeiro nome
nome = nome.split()
print('E seu primeiro nome tem ', len(nome[0]) , 'letras')



