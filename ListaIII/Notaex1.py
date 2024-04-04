nota = int(input(" Inisira uma nota, entre zero e dez: "))

while (nota > 10) or (nota < 0):
    nota = int(input("Valor Inválido! Insira um valor válido: "))

print("Nota válida")
