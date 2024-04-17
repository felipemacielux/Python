# ao invés de armazenar os dados através de index vai armazenar os dados em chaves

'''
x = {'nome' : 'Felipe', 'idade' : '21', 'profissão' : 'Programador' } #Pode se ter várias chaves e valores, sempre separados por dois pontos, do lado esquerdo nome do index e a direita o valor

print(x['idade']) # resgatando o valor da chave 'idade', chamando agora pelo valor ao invés do index

# Também pode ser adicionado novos dados

x['altura'] = '1.80' # adicionando um novo dado

print(x)

x = {'nomes': ['Felipe', 'Daniel', 'João', 'Douglas'], 'idades': [21, 22, 23, 24]}

print(x['nomes'][0])
'''

alunos = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]


notas = [aluno["nota"] for aluno in alunos] # é dado o comando para filtrar apenas as notas no dicionário
media = sum(notas) / len(notas) #abrindo a várial media, vai somar as notas e dividir por len notas que a quantidade de index em alunos
print(media)