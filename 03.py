cor_vermelha = '\033[91m'
reset_cor = '\033[0m'

def soma(v1, v2):
  return v1 + v2

def sub(v1, v2):
  return v1 - v2

def mult(v1, v2):
  return v1 * v2

def div(v1, v2):
  return v1 / v2

cases = {
  1: soma,
  2: sub,
  3: mult,
  4: div
}

while True:
  try:
    valor_1 = float(input('Informe o valor 1: ').replace(',', '.'))
    break
  except ValueError:
    print(cor_vermelha + 'Erro: Informe somente números!' + reset_cor)

while True:
  try:
    valor_2 = float(input('Informe o valor 2: ').replace(',', '.'))
    break
  except ValueError:
    print(cor_vermelha + 'Erro: Informe somente números!' + reset_cor)

while True:
  try:
    print("Selecione uma operação:")
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')

    operacao = int(input(''))

    if 1 <= operacao <= 4:
      funcao = cases.get(operacao)
      resultado = funcao(valor_1, valor_2)
      print('Resultado: ' + str(resultado))
      break
    else:
      print(cor_vermelha + 'Erro: Opção inválida!' + reset_cor)

  except ValueError:
    print(cor_vermelha + 'Erro: Informe somente números!' + reset_cor)
