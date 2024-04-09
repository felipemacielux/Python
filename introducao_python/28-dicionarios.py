# ao invés de armazenar os dados através de index vai armazenar os dados em chaves

'''
x = {'nome' : 'Felipe', 'idade' : '21', 'profissão' : 'Programador' } #Pode se ter várias chaves e valores, sempre separados por dois pontos, do lado esquerdo nome do index e a direita o valor

print(x['idade']) # resgatando o valor da chave 'idade', chamando agora pelo valor ao invés do index

# Também pode ser adicionado novos dados

x['altura'] = '1.80' # adicionando um novo dado

print(x)
'''
x = {'nomes': ['Felipe', 'Daniel', 'João', 'Douglas'], 'idades': [21, 22, 23, 24]}

print(x['nomes'][0])
