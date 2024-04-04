from random import sample
lista = sample(range(100), 20)
par = [x for x in lista if x % 2 == 0]
ímpar = [x for x in lista if x % 2 == 1]
print ('Vetor', lista)
print ('Pares', par)
print ('Ímpares', ímpar)


