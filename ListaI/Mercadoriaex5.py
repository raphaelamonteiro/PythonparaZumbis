mercadoria = float(input( "Digite o valor da mercadoria "))
desconto = int(input( "Digite o percentual de desconto "))
percentual = desconto * mercadoria
totaldesconto = percentual/100
mercadoriadesconto = mercadoria - totaldesconto
print (mercadoriadesconto, " valor com desconto")
