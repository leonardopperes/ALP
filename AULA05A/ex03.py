a = float(input("Digite o Lado 1: "))
b = float(input("Digite o Lado 2: "))
c = float(input("Digite o Lado 3: "))

if(((a+b)>c) and ((b+c)>a) and ((a+c)>b)):
    print ("Isso é um triangulo")
    if ((a == b) and (b == c)):
        print("Isso é um triângulo equilatero")
    elif ((a == b) or (a == c) or (b == c)):
        print("Isso é um triângulo Isósceles")
    else:
        print("Isso é um triangulo Escaleno")
else:
    print("Isso não é um triangulo")
