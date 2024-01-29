'''nomes = [3, 5, 27, 1, 2, 3, 15]

nomes_ordenados = sorted(nomes, reverse=True)
# para fazer com que retorne uma lista original e outra lista ordenada 
# print(sorted(nomes))


print(nomes_ordenados)


# Como acessar todos os valores de forma dinâmica através do laço for

idades = [3, 5 , 27, 1, 2, 3, 15]

for i in range(0, len(idades)): # len retorna o tamanho da lista idades, e o range serve para gerar uma lista e percorrer ela
    print(idades[i], i) # faz acessar um index de forma dinâmica atarvés de um for 

Ou pode ser feito da seguinte forma

'''

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