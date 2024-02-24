import ast

vetor_string = str(input('Informe um vetor com 10 posições: '))
vetor = ast.literal_eval(vetor_string)

if len(vetor) == 10:
  total_pares = 0
  total_impares = 0
  soma_pares = 0
  soma_impares = 0

  for i in range(0, 10):
    if vetor[i] % 2 == 0:
      total_pares += 1
      soma_pares += vetor[i]
    else:
      total_impares += 1
      soma_impares += vetor[i]

  media_impares = soma_impares / total_impares

  print('Total de pares: ' + str(total_pares))
  print('Total de impares: ' + str(total_impares))
  print('Soma dos pares: ' + str(soma_pares))
  print('Media dos impares: ' + str(media_impares))

else:
  print('Erro: Informe um vetor com 10 posições')
