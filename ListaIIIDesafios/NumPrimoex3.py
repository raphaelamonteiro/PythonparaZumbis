num = int(input("Digite um número: "))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if is_prime(num):
    print("O número é primo")
else:
    print("O número não é primo")
