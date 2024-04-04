conta = int(input("Conta: "))
pagamento = int(input("Pagamento: "))
troco = pagamento - conta
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
    while troco >= nota:
     print (f' Notas de {nota}')
    troco -= nota
