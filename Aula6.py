#Laços de repetiçoes

"""sorted_number = 15
choosen_number = int(input("informe seu número interiro entre 1 e 20: "))

while(choosen_number != sorted_number):
    print("você errou o número, tente novamente...")
    
    choosen_number = int(input("informe seu número interiro entre 1 e 20: "))
print("Você acertou!!")

contagem = 0

while contagem <= 20:
    print(contagem)
    contagem += 2

for variable in range(0, 11, 4): #(de onde começa, até -1, de quanto em quanto)
    print(variable)"""

media = 0
for i in range(1, 4):
    nota = float(input(f"Informe a sua nota {i}: "))
    media += nota
print(media/3)