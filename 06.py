import math

cor_vermelha = '\033[91m'
cor_verde = '\033[92m'
reset_cor = '\033[0m'

def primo(num):
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

while True:
  try:
    num = int(input('Informe um número: '))
    if num > 1 :
      break
    else:
      print(cor_vermelha + 'Erro: Informe um número maior que um!' + reset_cor)
  except ValueError:
    print(cor_vermelha + 'Erro: Informe somente números inteiros!' + reset_cor)


if primo(num):
  print(cor_verde + 'O número ' + str(num) + ' é primo' + reset_cor)
else:
  print(cor_vermelha + 'O número ' + str(num) + ' NÃO é primo' + reset_cor)
