peso = float(input("Digite o peso do peixe, em quilos: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print ("Excesso de: " , excesso)
    print( "Multa de: " , multa)
else:
    multa = excesso = 0
    print ("Excesso de: " , excesso)
    print( "Multa de: " , multa)
