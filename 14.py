matriz = []
for i in range(3):
  linha = []
  for j in range(4):
    vlr = str(input('Informe o valor da linha ' + str(i) + ' coluna ' + str(j) + ': '))
    linha.append(vlr)

  matriz.append(linha)

print("Matriz original: ")
for l in matriz:
  print(l)

print("Matriz transposta: ")

matriz_transposta = []
for j in range(4):
  linha_transposta = []
  for i in range(3):
    linha_transposta.append(matriz[i][j])
  matriz_transposta.append(linha_transposta)

for l in matriz_transposta:
  print(l)