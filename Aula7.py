#Estruturas de Listas

#Antes
nota1 = 9.8
nota2 = 7.8
nota3 = 6.0

#Com lista
notas = [9.8, 7.8, 6.0]

#Criando listas
notas = []      #lista vazia
lista = list()  #função list converte uma estrutura em uma lista
Dados = [19, "Miller", 3.14159, True]
lista_de_lista = [3, [1, 2, 3]]

#Indexação e Slices
print(Dados[0])     #primeiro elemento da lista começa indexadamente como 0
print(Dados[1])
print(Dados[2])
print(Dados[3])

    #Slices
list = [10, 20, 30, 40, 50, 60, 70]
print(list[0:3])
print(list[3:7])
print(list[2:])
print(list[0:7:2], "\n")

#Função len()
print("List len", len(list))
#Interações com For

#Utilizando os próprios elementos da lista
for element in list:
    print(element)
print("\n")

#Utilizando os índices
for i in range(len(list)):
    print(list[i])
