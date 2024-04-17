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


# Lê números inteiros colocados pelos usuários


#Lista a partir desses números

numeros = int(input("Quantos números você vai digitar:  "))

listas = [] 
for i in range(numeros): # Nesse caso vai gerar uma sequência de números até o especificado pelo usuário na entrada de dados acima
    lista = int(input("Digite um número para receber a lista ou -1 para sair: "))
    if lista == "-1":
        break   

    
    listas.append(lista)


print(listas)
    


lista = [1, 10, 20, 35, 22, 12]

soma = 0 

for i in lista:
    soma += i

print(soma)
        




lista = [1, 10, 20, 35, 22, 12]

media = 0
soma = 0
for i in lista:
    media += i
    soma += 1
    
    
 
print (media//soma)


alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9),
]

notas = [nota for nome, nota in alunos]  #loop que vai percorrer a lista alunos e vai descompactar em duas váriaveis como nota e nome chamado de descompactamento de tuplas, colocando primeiro o elemento nome e o segundo como nota, na mesma ordem da linha de código
media = 0
soma = 0
for i in notas:
    media += i
    soma += 1

print(media//soma)
'''

palavra = (input("Digite uma palavra: "))
letras = list(palavra.lower()) #list = cria uma lista com a palavra digitada pelo usuário e as separa as letras lower = converte ela para minuscula
contagem_letras = {} # Dicionário para rastrear a contagem de cada letra/ Nesse código, o dicionário contagem_letras armazena a contagem de cada letra (ignorando caracteres não alfabéticos)

for letra in letras: # vai percorrer cada letra na lista letras
    if letra.isalpha():  # Verifica se é uma letra do alfabeto
        if letra in contagem_letras: # Verifica se a letra já está presente no dicionário contagem_letras/ Se a letra já estiver no dicionário, incrementamos sua contagem.
            contagem_letras[letra] += 1 # Se a letra não estiver no dicionário, adicionamos uma entrada com a letra como chave e inicializamos a contagem como 1.
        else:
            contagem_letras[letra] = 1

for letra, contagem in contagem_letras.items(): # letra = Essa variável recebe a chave do dicionario 
    #contagem recebe: a contagem de quantas vezes a letra aparece
    print(f"A letra '{letra}' aparece {contagem} vezes.")
