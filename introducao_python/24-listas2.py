'''
Insert

nomes = ['Felipe', 'Daniel', 'Joao', 'Douglas']
# Tem como adicionar em uma posição especifica
nomes.insert(2, 'Maria') # Sempre a posição e depois da virgula o dado que vai ser adicionado
print(nomes)


#Excluir os dados de uma lista

nomes = ['Felipe', 'Daniel', 'Joao', 'Douglas']
nomes.pop(0) #o pop sempre remove o último dado da lista ou se não passar uma posição especifica, ele só remove se for passado um index, ou seja, um número de posição
# Já o remove ele remove o dado da lista com o nome do dado que foi passado

print(nomes)



# Como descobrir qual index está determinado elemento

nomes = ['Felipe', 'Daniel', 'Joao', 'Douglas']
print(nomes.index('Joao'))
'''

#Ordenar a lista em alfabética ou de números

nomes = ['Felipe', 'Daniel', 'Joao', 'Douglas']

nomes.sort(reverse=True) #reverse true serve para inverter a ordem
#sorted serve para ordenar e retornar uma lista ordenada, ou seja, fica com uma lista original e uma lista ordenada
#Aqui no caso ficará com uma lista que altera a propria lista no caso

print(nomes)
