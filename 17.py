def organizar_crescente(vet):
  crescente = vet
  aux = 0
  
  for i in range(9):
    for j in range((i+1), 10):
      if crescente[i] > crescente[j]:
        aux = crescente[j]
        crescente[j] = crescente[i]
        crescente[i] = aux

  return crescente

def organizar_decrescente(vet):
  decrescente = vet
  aux = 0
  for i in range(9):
    for j in range((i+1), 10):
      if decrescente[i] < decrescente[j]:
        aux = decrescente[j]
        decrescente[j] = decrescente[i]
        decrescente[i] = aux
  return decrescente

vetor = []
for i in range(10):
  vlr = int(input('Informe um valor inteiro: '))
  vetor.append(vlr)

print(organizar_crescente(vetor))
print(organizar_decrescente(vetor))
