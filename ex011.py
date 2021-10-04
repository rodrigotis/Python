# Desafio 011 = crie um programa que leia a largura
# e a altura de uma parede em metros e calcule a sua área
# e a quantidade de tinta necessária para pintar
# sabe-se que cada litro de tinta pinta 2m²

l = float(input('Qual é a largura da parede? '))
a = float(input('e agora a altura dela? '))
m2 = l * a #calculo de área Largura * altura
t = m2/2

print(f'Com uma largura de {l} metros e altura de {a} metros,\n'
      f'a parede em questão tem uma área de {m2} m².\n'
      f'Para pintar esta parede, será necessário {t} litros de tinta!')