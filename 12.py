import random

vetor = []

count_num = 0

for i in range(0, 1000):
  numero_aleatorio = random.randint(0, 1000)
  vetor.append(numero_aleatorio)
  if numero_aleatorio >= 700:
    count_num += 1

# print('Total de numeros maiores ou igual a 700: ' + str(count_num))
porcentagem = (count_num*100)/1000
print('Porcentagem >= 700: ' + str(porcentagem) + '%')
