lado1 = int(input("Insira o primeiro lado do triângulo: "))
lado2 = int(input("Insira o segundo lado do triângulo: "))
lado3 = int(input("Insira o terceiro lado do triângulo: "))
if (lado1 == lado2 == lado3):
    print ("Este triângulo é equilátero")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print ("Este triângulo é isóceles")

else:
    print ("Este triângulo é escaleno")
