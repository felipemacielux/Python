'''

# Iterando sobre uma lista e calculando a média


notas = [85, 90, 75, 88, 92] # criação da lista
soma = 0 # variável para acumular a soma das notas
for nota in notas: # laço em que vai percorrer cada elemento da lista
    soma += nota # acumula a nota (ou seja, vai ficar somando a cada iteração)
media = soma / len(notas) # calcula a média (vai pegar o resultado da soma e dividir pela quantidade de indexes da lista)
print("Média das notas:", media)

# Lista de listas para representar uma grade de dados

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Grade de dados:")
for linha in grid:
    print(linha)

# Lista de dicionários para representar registros de banco de dados
registros = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 35}
]
for registro in registros:
    print("Nome:", registro["nome"], "- Idade:", registro["idade"])


# Escreva um programa que receba uma lista de números do usuário e retorne o maior número da lista.
    
numeros = [] # Criando a lista vazia

while True: # Loop infinito
    numero = int(input("Digite um número (ou 0 para encerrar): ")) # Recebendo um número do usuário
    if numero == 0: # Se o número for 0, encerra o loop
        break
    numeros.append(numero) # Adiciona o número na lista

maior = max(numeros) # Calcula o maior número
print("O maior número da lista é:", maior)


#Escreva uma função que receba uma lista de números e retorne a soma de todos os números ímpares na lista.

numeros = []
while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    if numero == 0:
        break
    numeros.append(numero)
# No código acima é criado uma lista vazia em que o usuário vai armazenar os números, quando o laço for interrompido vai passar para soma
soma = 0
for numero in numeros:
    if numero % 2 == 1:
        soma += numero
print("A soma de todos os números ímpares da lista é:", soma)

#Acima é possível ver que o loop vai percorrer a lista criada pelo usuário depois vai dividir por 2 e verificar se o resto da divisão é 1. Se for 1, o número é ímpar e vai armazenar na váriavel soma, até percorrer toda lista.
'''

numeros = []
while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    if numero == 0:
        break
    numeros.append(numero)

soma = 0
for numero in numeros:
    if numero % 2 == 1:
        soma += numero
print("A soma de todos os números ímpares da lista é:", soma)