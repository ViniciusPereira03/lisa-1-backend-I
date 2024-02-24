import random

cor_vermelha = '\033[91m'
cor_verde = '\033[92m'
reset_cor = '\033[0m'

numero_aleatorio = random.randint(0, 9)
tentativas = 1

while True:
  try:
    num = int(input('Informe um número: '))

    if num == numero_aleatorio:
      print(cor_verde + 'Você acertou o número ' + str(num) + ' sorteado em ' + str(tentativas) + ' tentativas!' + reset_cor)
      break
    else:
      tentativas += 1
      print(cor_vermelha + 'Número errado, tente novamente!' + reset_cor)

  except ValueError:
    print(cor_vermelha + 'Erro: Informe somente números inteiros!' + reset_cor)
