cor_vermelha = '\033[91m'
reset_cor = '\033[0m'

def tabuada(valor):
  for num in range (1, 11):
    print(str(num) + ' X ' + str(valor) + ' = ' + str(num*valor))
  print(' ')

while True:
  try:
    valor_1 = int(input('Informe o valor 1: '))
    if valor_1 > 0 :
      break
    else:
      print(cor_vermelha + 'Erro: Informe um número maior que zero!' + reset_cor)
  except ValueError:
    print(cor_vermelha + 'Erro: Informe somente números inteiros!' + reset_cor)

while True:
  try:
    valor_2 = int(input('Informe o valor 2: '))
    if valor_2 > 0:
      if valor_1 != valor_2:
        break
      else:
        print(cor_vermelha + 'Erro: Informe um número diferente do primeiro!' + reset_cor)
    else:
      print(cor_vermelha + 'Erro: Informe um número maior que zero!' + reset_cor)
  except ValueError:
    print(cor_vermelha + 'Erro: Informe somente números inteiros!' + reset_cor)

for num in range (valor_1, valor_2+1):
  tabuada(num)
  