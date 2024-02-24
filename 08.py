cor_vermelha = '\033[91m'
cor_verde = '\033[92m'
reset_cor = '\033[0m'

def validar_cpf(cpf):

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma_1 = sum(int(cpf[i]) * (10 - i) for i in range(9)) % 11
    digito_1 = 0 if soma_1 < 2 else 11 - soma_1

    soma_2 = sum(int(cpf[i]) * (11 - i) for i in range(10)) % 11
    digito_2 = 0 if soma_2 < 2 else 11 - soma_2

    return int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2


while True:
  try:
    cpf = int(input('Digite o CPF: '))
    break
  except ValueError:
    print(cor_vermelha + 'Erro: Informe somente números!' + reset_cor)

if validar_cpf(str(cpf)):
  print(cor_verde + 'CPF válido.' + reset_cor)
else:
  print(cor_vermelha + 'CPF inválido.' + reset_cor)
