vh = float(input("Insira o valor da sua hora trabalhada: "))
ht = float(input("Insira quantas horas por mês você trabalha: "))
sb = vh * ht
inss = sb * 0.1
#calculo do imposto de renda
if sb <=900:
    ir = 0
    aliquota = 0
elif sb <= 1500:
    ir =  sb*0.05
    aliquota = 5
elif sb <= 2500:
    ir = sb*0.10
    aliquota = 10
else:
    ir = sb * 0.2
    aliquota = 20
fgts = sb*0.11
sind = sb*0.03
td = inss + ir
sl = sb - td
print("Salário bruto: (", vh,"*", ht, ")       : R$",sb)
print("(-) IR(",aliquota,"%)                         : R$",ir)
print("(-) INSS(10%)                         : R$",inss)
print("FGTS(11%)                             : R$",fgts)
print("Total de descontos                    : R$",td)
print("Salário Líquido                       : R$",sl)
