#conjuntos em python, tudo que é colocado de forma repetida ele não aparece o dado repetido

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto2 = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}


conjunto_uniao = conjunto.union(conjunto2)#  o conjunto.union vai unir os dois conjuntos e armazenar no conjunto_uniao

conjunto_uniao = conjunto.intersection(conjunto2) # o conjunto.intersection vai mostrar apenas os dados que existem em ambos os conjuntos

conjunto_uniao = conjunto.difference(conjunto2)# conjunto.difference vai mostrar os dados que existem apenas no conjunto

print(conjunto_uniao)

#tem como adicionar dados como em listas, mas não possuem ordens
