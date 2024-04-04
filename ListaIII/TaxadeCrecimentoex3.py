populaçãoA = 80000
populaçãoB = 200000

crescimentoA = 0.03
crescimentoB = 0.015

anos = 0
while populaçãoA <= populaçãoB:
    populaçãoA = populaçãoA + (populaçãoA * crescimentoA)
    populaçãoB = populaçãoB + (populaçãoB * crescimentoB)
    anos = anos + 1

print (anos)

