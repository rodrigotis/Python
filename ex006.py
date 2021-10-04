# Desafio 006 = Crie um algoritmo que leia um número e mostre seu dobro
# , triplo e raiz quadrada

n = int(input('Escolha um número: '))
d = n*2
t = n*3
r = n**(1/2) # outra alternativa para raiz = pow(n,expoente)

print(f'Jóia! Vamos lá!\n\nVocê escolheu o número {n}, correto?\n'
      f'Você sabia que o dobro dele é {d}?\n'
      f'O triplo é {t} e\n'
      f'a raiz quadrada dele é {r:.2f}!\n' 
#mesmo com o format simplificado é possível configurar a saída dos dados)
      f'Louco né?')