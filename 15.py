def crivo_eratostenes(n):
  primos = [True] * (n + 1)
  primos[0] = primos[1] = False

  for i in range(2, int(n**0.5) + 1):
    if primos[i]:
      for j in range(i*i, n+1, i):
        primos[j] = False

  return [x for x in range(2, n+1) if primos[x]]

def print_matriz(marcador='*'):
  limite = 100
  primos = crivo_eratostenes(limite)
  
  for i in range(1, limite+1):
    if i in primos:
      print(marcador, end=' ')
    else:
      print(i, end=' ')
    
    if i % 10 == 0:
      print()

print_matriz()
