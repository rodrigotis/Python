# Desafio 032 = faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
## Regras do Bissexto:
### condição 1 se o ano não terminar em 00, deve ser dividido por 4
### condição 2 se o ano terminar 00 devem ser divisiveis por 400 e o resto ser igual a 0
# Resolução extra
## adicionando funcionalidade que lê o ano atual
from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')