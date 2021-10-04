# Desafio 031 = Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0.5 por Km para viagens até 200km e R$ 0.45
#para viagens mais longas

# Desenvolva um programa que pergunte a distância de uma viagem em KM.
d = float(input('Caro passageiro, sua viagem será de quanto Km? (APENAS NÚMEROS) '))

# t1 será a taxa/Km em viagens até 200 km
t1 = d * 0.5
# t2 será a taxa/km em viagens maiores que 200 km
t2  = d * 0.45

#Calcule o preço da passagem
if d <= 200:
    print(f'Passageiro, sua viagem de {d}Km irá custar R${t1:.2f}\n'
          f'Obrigado pela preferência!!')
else:
    print(f'Passageiro, sua viagem de {d}Km irá custar R${t2:.2f}\n'
          f'Obrigado pela preferência!!')
# é possivel simplificar o if:
#preço = distância * 0,5 if distância <= 200 else distância * 0,45