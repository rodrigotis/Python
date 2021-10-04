# Desafio 032 = faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
## Regras do Bissexto:
### condição 1 se o ano não terminar em 00, deve ser dividido por 4
### condição 2 se o ano terminar 00 devem ser divisiveis por 400 e o resto ser igual a 0

ano = str(input('Escolha um ano qualquer: '))
print(f'O ano escolhido foi: {ano}')


if ano[2] + ano[3] != '00':
    ano = int(ano)
    if ano % 4 == 0:
        print('E ele é um ano bissexto')
    else:
        print('E ele não é um ano bissexto')

ano = str(ano)

if ano[2] + ano[3] == '00':
    ano = int(ano)
    if ano % 400 == 0:
        print('E ele é um ano bissexto')
    else:
        print('E ele não é um ano bissexto')
