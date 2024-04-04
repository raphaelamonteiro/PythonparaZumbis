metros = float(input("Tamanho em metros quadrados da área a ser pintada: "))
litros = metros / 3
latas = litros / 18
preço = latas * 80.00

print (f'{latas:.2f} latas de tinta serão necessárias para pintar a área')
print (f'{preço:.2f} reais, no total')
