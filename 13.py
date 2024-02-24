def matriz_1():
    matriz = []
    for i in range(10):
      linha = []
      for j in range(10):
        linha.append(str(i) + str(j))
      matriz.append(linha)
    return matriz

def matriz_2():
  matriz = []
  for i in range(10):
    linha = []
    for j in range(10):
      valor = 0
      
      if i == j:
        valor = 1
      elif i > j:
        valor = 2

      linha.append(valor)
    matriz.append(linha)  
  return matriz

matriz_original = matriz_1()
segunda_matriz = matriz_2()

for linha in matriz_original:
    print(linha)

print('')

for linha in segunda_matriz:
    print(linha)
