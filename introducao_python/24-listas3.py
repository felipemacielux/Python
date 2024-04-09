nomes = [3, 5, 27, 1, 2, 3, 15]

nomes_ordenados = sorted(nomes, reverse=True)
# Aqui faz com que a lista nomes fique inalterada e cria nomes_ordenados para criar uma outra lista
# print(sorted(nomes))


print(nomes_ordenados)

'''
# Como acessar todos os valores de forma dinâmica através do laço for

idades = [3, 5 , 27, 1, 2, 3, 15]

for i in range(0, len(idades)): # len retorna o tamanho da lista idades, e o range serve para gerar uma lista e percorrer ela
    print(idades[i], i) # faz acessar um index de forma dinâmica atarvés de um for 

Ou pode ser feito da seguinte forma



idades = [3, 5 , 27, 1, 2, 3, 15]

#for i in idades:
    #print(i) # só que dessa forma não tem como acessar o index

    # o enumerate gera uma lista de tuplas, com o index e o valor da lista

for i, v in enumerate(idades): # O v significa valor e o i o index 
    print(i, v)


# para saber os números pares dessa lista
    
idades = [3, 5 , 27, 1, 2, 3, 15, 60, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

idades_pares = [] # tem que chamar vazio para poder adicionar os valores

for i in idades:
    if i % 2 == 0:
        idades_pares.append(i)# isso faz com que o valor seja adicionado na lista, apenas se ele for par

print(idades_pares)

'''

notas = [8, 10, 7, 6.5] #acumulando os números na lista

i = 0 # vai acumulando sempre que o laço for true
total = 0 # vai acumulando as somas das notas

qtd = len(notas) # com o len é possível que lê a quantidade de itens da lista sem precisar passar precisamente os números precisos, caso seja adicionado mais um número na lista ele vai pegar por essa várialvel que está sendo utilizado o len

while i < qtd:  # enquantro true, faz o calculo abaixo
    total = total + notas [i] # vai incrementar sempre o valor do total com cada index da lista
    i =+ 1

print("O total das notas é:", total)

media = total / qtd #pegar o total de todos os itens somados e dividir por 5
print("A média é:", media)