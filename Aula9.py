#Funções

####Criação de funções

#função inicial
def hello():
    print("Seja bem-vindo(a)!")
    print("É um prazer tê-lo por aqui")

hello()

#Funçãp com parâmetros
def Ola(nome, local):
    print(f"Seja bem-vindo(a) {nome}!")
    print(f"É um prazer tê-lo por aqui em {local}")
    


#Função com parêmetros Default
def Hola(nome, local="Fortaleza"):
    print(f"Seja bem-vindo(a) {nome}!")
    print(f"É um prazer tê-lo por aqui em {local}")
    

#Função com retorno
def soma(num1, num2):
    return int(num1 + num2)

resultado = soma(int(input()), int(input()))
print(resultado)