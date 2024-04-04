trabalho = int(input("Insira o número de horas trabalhadas no mês: "))
ganho = float(input("Insira o valor recebido por hora: "))

salariobruto = trabalho * ganho
ir = salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05
salarioliquido = salariobruto - ir - inss - sindicato

print (f'+ Salário Bruto: R$ {salariobruto:.2f}')
print (f'-Imposto de Renda: R$ {ir:.2f}')
print (f'-INSS: R$ {inss:.2f}')
print (f'-Sindicato: R$ {sindicato:.2f}')
print (f'=Salário Líquido: , R$ {salarioliquido:.2f}')
