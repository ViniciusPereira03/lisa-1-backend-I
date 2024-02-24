def determinante(matriz):
  det = 0

  for i in range(3):
    det += matriz[0][i] * matriz[1][(i + 1) % 3] * matriz[2][(i + 2) % 3]
    det -= matriz[2][i] * matriz[1][(i + 1) % 3] * matriz[0][(i + 2) % 3]

  return det
                                                                             

matriz = []
for i in range(3):
  linha = []
  for j in range(3):
    vlr = int(input('Informe o valor da linha ' + str(i) + ' coluna ' + str(j) + ': '))
    linha.append(vlr)

  matriz.append(linha)

print("Matriz: ")
for l in matriz:
  print(l)

det = determinante(matriz)
print("Determinante: " + str(det))
