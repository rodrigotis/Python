# Desafio 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7.00 por cada km acima do limite

# a) Escreva um programa que leia a velocidade de um carro.

v = int(input('Qual é a velocidade do seu veículo agora ? (Apenas os números?)  '))
# Se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7.00 por cada km acima do limite

m = 7.00 * (v-80)

if v <= 80:
    print (f'Ok, com {v} Km/h você está dentro do limite.')
else:
    v + m
    print(f'Temos um problema: sua velocidade está em {v} km por hora,\n'
          f'isso ultrapassa o limite de 80 Km/h.\n'
          f'a multa por excesso de velocidade será de: R$ {m:.2f}')
print('Tenha um bom dia e dirija com segurança!')

