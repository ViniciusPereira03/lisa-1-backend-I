import getpass

cor_vermelha = '\033[91m'
cor_verde = '\033[92m'
reset_cor = '\033[0m'

login = 'IFSP'
senha = 'PosWEB'

tentativa = 1
isLogged = False

while tentativa <= 3:
  login_input = str(input('Login: '))
  senha_input = getpass.getpass("Senha: ")

  if (login == login_input) and (senha == senha_input):
    print(cor_verde + 'Login efetuado com sucesso' + reset_cor)
    isLogged = True
    break
  else:
    print(cor_vermelha + 'Login ou senha incorreta' + reset_cor)
  
  tentativa += 1

if isLogged == False:
  print(cor_vermelha + 'Acesso negado!' + reset_cor)
