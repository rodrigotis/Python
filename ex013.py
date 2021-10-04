# desafio 013 = faça um algoritmo que leia o salário de um funcionário e mostre seu
# salário com acréscimo de 15%

n = input('Qual o nome do(a) funcionário(a)? ')
s = float(input('Qual é seu salário? R$ '))
s2 = s * 0.15 + s
print(f'Incrível! Avise \033[1;36;40m{n}\033[m que houve um aumento \n'
      f'em seu salário e passará a ganhar R$ \033[7;32;40m{s2:.2f}\033[m por mês!!')
