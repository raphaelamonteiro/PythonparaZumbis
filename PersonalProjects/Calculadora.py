n1 = int(input("Insira o 1° número: "))
n2 = int(input("Insira o 2° número: "))
action = str(input("Escolha a operação: Adição(a), Subtração(s), Multiplicação(m), Divisão(d)->"))
90
print("O resultado é:", end="")
if action == "a":
    print(n1 + n2)

elif action == "s":
      print(n1 - n2)

elif action == "m":
      print(n1 * n2)

elif action == "d":
      print(n1 / n2)
