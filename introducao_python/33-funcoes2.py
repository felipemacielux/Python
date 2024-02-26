'''

# Como passar argumentos em uma função

def soma_numeros(n1, n2): #Vai receber dois valores quando for chamada e vai somar esses valores
    # O def significa definir, ou seja, vai definir a função
    print(n1 + n2)

soma_numeros(10, 5)# Pode ser chamada varias vezes a função, passando valores diferentes
'''

def soma_numeros(*args): # utilizado quando o usuario vai passar quantos argumentos quiser e não se sabe quantos foram passados
    print(sum(args))

soma_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# ou pode ser feito dessa maneira

def soma_numeros2 (*args):
    soma = 0
    for i in args: # Loop for que vai interar por todos os argumentos que foram passados quando a função foi chamada em baixo
        soma += i
    print(soma)
soma_numeros2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def mostrar_informacoes(**kwargs): # é tratado como dicionário, onde são armazenados as chaves e os nomes dos argumentos
    for chaves, valor in kwargs.items(): # kwargs.items retorna uma visão dos itens do dicionário e o loop for serve para iterar cada chave e valor colocados no dicionário
        print(f'{chaves}: {valor}') # vai mostrar as chaves e os valores

mostrar_informacoes(nome='Felipe', idade=21, profissão='Programador')