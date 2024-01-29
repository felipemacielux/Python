'''


# matrizes e listas de listas

idades = [

            [3, 5, 27, 1, 2, 3, 15], #linha número 0
            [16, 8, 13, 2, 3, 4, 1], # linha 1
            [23, 4, 5, 6, 7, 8, 9] # linha 2

] # criar uma lista onde terá linhas e colunas, mas deve ter o mesmo número de linhas e colunas    

print(idades[0][2]) #primeiro passa a linha e depois a coluna

'''

idades = [

            [3, 5, 27, 1, 2, 3, 15], #linha número 0
            [16, 8, 13, 2, 3, 4, 1], # linha 1
            [23, 4, 5, 6, 7, 8, 9] # linha 2

]

for i in range(0, len(idades)): # Aqui vai percorrer todas as linhas da lista
    for j in range(0, len(idades[i])): # ele vai iterar os elementos de cada linha
        print(idades[i][j]) 