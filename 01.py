import os

os.system('cls')
nome = str(input('Informe o nome do cliente: '))

while True:
  try:
    valor_compra = float(input('Informe o valor da compra: ').replace(',', '.'))
    valor_compra = f"{valor_compra:.2f}"
    break
  except ValueError:
    print('Erro: Informe somente números!')

rua = str(input('Informe a rua: '))

data_entrega = str(input('Informe a data da entrega: '))

os.system('cls')

print('')
print('                              AVISO')
print('Caro cliente Sr(a) ' + nome + ', os produtos da sua compra no')
print('valor de R$ ' + str(valor_compra).replace('.', ',') + ' serão entregues no endereço abaixo:')
print('Rua ' + rua + '.')
print('Data da Entrega: ' + data_entrega + '.')
print('******************** Obrigado pela Preferência! **********************')
print('')
