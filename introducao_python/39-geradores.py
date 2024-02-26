from pympler.asizeof import asizesof

'''
print(asizesof(1)) # mostra a quantidade de memoria alocada para o objeto 1 (vai printar o que gasta que são 32 bits) 

def dobro(lista): #definindo uma função
    lista_dobro = [] #criando uma lista vazia
    for i in lista: #inicia um loop for que vai percorrer cada elemento da lista
        lista_dobro.append(i*2)# para cada elemento vai ser adicionado o valor multiplicado por 2 na lista_dobro
    return lista_dobro

x = asizesof(dobro(range(0, 100000))) # está chamando a função dobro que vai criar uma sequencia de 0 até 99999
#o asizesof retorna o tamanho do objeto em bytes

print((x))


def dobro(lista):
    return 1


print(dobro) # vai aparecer função de dobro e onde está alocada na memória

'''

def dobro():
    yield 1 # chave utilizada para criar um gerador, que vai retornar os valores de 1

print(next(dobro())) #quando a função next é chamada ela deve retornar o primeiro número primo que começa por 1 (gera uma instância)