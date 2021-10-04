# DESAFIO 3: Solicitar a inclusão de números pelo teclado, some-os e printe o resultado
# de forma completa

# importante: por ser uma soma, deve-se alterar o tipo de dados de string (str) para inteiro (int).
# para isso, basta incluir a função int e, dentro desta função, inserir os input

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}.'.format(n1, n2, s))
# novamente, utilizando máscaras e a função format para automatizar o prog.