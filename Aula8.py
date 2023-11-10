#Métodos de listas

list = [1, 3, 12, 8, 2]

#append
print("Antes do append", list)
list.append(17)
print("Depois do append", list)

#insert
list.insert(1, 12) #(posição, dado a inserir)
print("depois do insert", list)

#extend             une duas lista (uma no final da outra)
lista2 = [2, 17]

list.extend(lista2)
print("Depois do extend", list)
print(list)

#pop            remove um elemento se especificado, se não, remove o último elemento
lista2.pop()
print("lista2 apos ser popada", lista2)
list.pop(1)
print("list apos popar o segundo elemento[1]", list)

#remove        remove o elemento especificado de menor índice da lista
list.remove(1)
print("list apos remover 1", list)

#count         conta a quantidade de repetições na lista do elemento especificado
print("Quantidade de vezes que 17 aparece: ", list.count(17))

#index          mostra qual o índice do elemento especificado
print("indice do elemento 12: ", list.index(12))

#sort           ordena a lista
list.sort()
print(list)



#Funções para listas

#len            indica o tamanho da lista
print(len(list))

#sum            realiza a soma dos elementos da lista numérica
print(sum(list))    

#max            indica o maior elemento da lista numérica
print(max(list))

#min            indica o menor elemento da lista numérica
print(min(list))