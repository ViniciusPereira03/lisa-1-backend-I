import os

while True:
  try:
    altura = float(input('Informe sua altura: ').replace(',', '.'))
    break
  except ValueError:
    print('Erro: Informe somente números!')

while True:
  try:
    peso = float(input('Informe seu peso: ').replace(',', '.'))
    break
  except ValueError:
    print('Erro: Informe somente números!')

os.system('cls')

resultado_imc = peso / (altura*altura)

if resultado_imc < 16.5:
  print('Resultado: Desnutrição')
elif resultado_imc <= 18.5:
  print('Resultado: Abaixo do peso')
elif resultado_imc <= 24.9:
  print('Resultado: Peso normal')
elif resultado_imc <= 29.9:
  print('Resultado: Sobrepeso')
else:
  print('Resultado: Obesidade')

