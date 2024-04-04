n = int(input("Digite um número: "))

a, b = 1, 1
F = 1

while F <= n-2:
    a, b = b, a + b
    F = F + 1

print (b)
