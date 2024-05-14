#Imprimir os números pares entre 0 e um número fornecido usando if

fim = int(input("Digite o último numero: "))
x = 0
while x <= fim:
  if x % 2 == 0:
    print (x)
  x = x + 1

#sem o if
fim = int(input("Digite o último numero: "))
x = 0
while x <= fim:
  print(x)
  x = x + 2
