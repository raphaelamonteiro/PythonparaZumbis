cigarros =  int(input("Quantidade de cigarros fumados por dia: "))
anos = int(input("Digite os anos: "))
totalcigarros = anos * 365 * cigarros
dias = totalcigarros / 144
print ((round(dias)), "  dias foram perdidos")
