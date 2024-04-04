num = int(input("Insira o número: "))
for k in range(2, num):
  while num % k == 0:
    print (k)
    num = num / k


