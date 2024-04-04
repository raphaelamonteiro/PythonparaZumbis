from random import sample
vetor = sample(range(100), 10)
maior = menor = vetor[0]
for num in vetor[1:]:
  if num > maior: maior = num
  if num < menor: menor = num
print ('Vetor:', vetor)
print (f'Maior: {maior}')
print (f'Menor: {menor}')



