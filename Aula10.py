#Dicionários

#Criando Dicionários
dicionario = {}
dicionario = dict()

dicionario = {"nome": "Miller", "idade": 20, "altura": 1.79}
print(dicionario)
print(dicionario["idade"])

#Adicionando elementos no Dicionário

dicionario["programador"] = True
print(dicionario)

dicionario["idade"] = 19
print(dicionario)

#Iterando sobre um dicionaraio
for key in dicionario:
    print(key, dicionario[key])
    
#Testando a existência de uma chave
print("peso" in dicionario)
print("altura" in dicionario)