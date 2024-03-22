n1 = float(input("Forneça a primeira nota:"))
n2 = float(input("Forneça a segunda nota:"))
media = (n1+n2)/2
if(media>=9.0) and (media<=10.0):
    conceito = "A"
    situação = "Aprovado"
elif(media>=7.5) and (media<9.0):
    conceito = "B"
    situação = "Aprovado"
elif(media>=6) and (media<7.5):
    conceito = "C"
    situação = "Aprovado"
elif(media>=4.0) and (media<6.0):
    conceito = "D"
    situação = "Reprovado"
else:
    conceito = "E"
    situação = "Reprovado"

print("Suas notas foram",n1,"e",n2)
print("Seu conceito é: ",conceito)
print("Você está: ",situação)

