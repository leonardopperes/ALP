a = float(input("Digite o Lado 1: "))
b = float(input("Digite o Lado 2: "))
c = float(input("Digite o Lado 3: "))

if(((a+b)<c) or ((b+c)<a) or ((a+c)<b)):
    print ("Isso não é um triangulo")
else:
    print("Isso é um triangulo")

if((a==b) and (b==c)):
    print("Isso é um triângulo equilatero")
elif((a==b) or (a==c) or (b==c)):
    print("Isso é um triângulo Isósceles")
else:
    print("Isso é um triangulo Escaleno")
