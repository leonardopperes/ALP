import math
c = float(input("Digite o comprimento do aposento: "))
l = float(input("Digite a largura do aposento: "))
t = float(input("Digite a quantidade de Litros em uma lata: "))
h = 2.80
at = ((2*c*l)+(2*c*h)+(2*h*l))
des = 0.8*2.1
au = at - des
cobre = 3
quant = (au/cobre)
print("Você terá que cobrir um total de",round(au,2),"metros quadrados e fará uso de",round(quant,2),"litros de tinta")
if t == 1:
    print("Você precisa comprar ao menos:", math.ceil(quant/1),"latas de 1L")
elif t == 18:
    print("Você precisa comprar ao menos:", math.ceil(quant/18),"latas de 18L")
elif t == 3.7:
    print("Você precisa comprar ao menos:", math.ceil(quant/3.7), "latas de 3,7L")
else:
    print("Porém, não possuímos nenhuma lata com essa quantidade de litros")
