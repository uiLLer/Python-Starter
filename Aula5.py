#Estruturas Condicionais
idade = int(input("Digite sua idade:"))
if idade >= 18:
    print("Você é maior de idade")
else:
    print("VOcê é menor de idade")
    
Nota_1 = float(input("Digite sua primeira nota "))
Nota_2 = float(input("Digite sua segunda nota "))
Nota_3 = float(input("Digite sua terceira nota "))
Nota_4 = float(input("Digite sua quarta nota "))

media = (Nota_1 + Nota_2 + Nota_3 + Nota_4)/4


if media >= 7:
    print("sua média foi ", media, " e Você foi aprovado")
elif media >= 5:
    print("sua média foi ", media," e você vai para a recuperação")
else:
    print("sua média foi ",media,"e você foi reprovado")
    
