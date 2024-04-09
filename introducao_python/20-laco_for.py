'''
Diferença entre o laço for e laço while

while -> Tudo que for fazer com laço for tem como fazer com laço while
Utilizado quando você não sabe quantas vezes seu laço irá rodar
for -> Possui algumas limitações



for i in range(0, 5): #para i em um intervalo de 0 a 5 (mas o 5 não entra e ele iria até o 4) ele vai até o valor -1
    print(i)

#Senão quiser que chega de um número a tal número muito grande, o ideal é trabalhar com intervalos, esses intervalos para pular de 2 em 2 e assim por diante são nomeados como step, e são colocados na "terceira" casa

for i in range(0, 100, 2): #Aqui nesse caso ele está indo de 2 em 2, definindo um intervalo de tempo
    print(i)


Para ordem decrescente:

for i in range(100, 0, -1): 
    print(i)

Tem que ser ao inverso

print(list( range(100, 0, -1) ))

iterando

Da para percorrer mesmo sendo caracter (string)




x = input("Digite seu nome: ")

for i in x:
    print(i)


# Se for rodar o loop numa iteração de dicionários ele vai pegar como base apenas a chave, a não ser que especifica ele
'''

# Lê números inteiros colocados pelos usuários
n1 = int(input("Digite um número para receber a lista: "))

n1 = [] #Todos os números criado pelo usuário serão armazenados nessa lista

#Lista a partir desses números
for i in n1:
    if n1 == -1:
        print ("Deseja continuar a lista?")



# Imprime a lista montada




# Poderá continuar montando listas e mais listas até o usuário digitar -1 para sair
