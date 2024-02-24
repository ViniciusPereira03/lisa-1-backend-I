cor_vermelha = '\033[91m'
cor_verde = '\033[92m'
reset_cor = '\033[0m'

def calcularFatorial(num):
  if num == 1:
    return num * 1
  else:
    return num * calcularFatorial(num-1)

while True:
  try:
    num = int(input('Informe um numero inteiro: '))
    break
  except ValueError:
    print(cor_vermelha + 'Erro: Informe somente números inteiros!' + reset_cor)

fatorial = calcularFatorial(num)
print(str(num) + '! = ' + str(fatorial))