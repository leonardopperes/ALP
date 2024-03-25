v = float(input("Digite o valor da compra: "))
if v <= 1000.00:
    print("Você deverá pagar:",v*0.9)
    print("Desconto é igual: 10%")
elif (v > 5000):
    print("Você deverá pagar:", v * 0.7)
    print("Desconto é igual: 30%")
else:
    print("Voce deverà pagar:", v * 0.8)
    print("Desconto é igual: 20%")

