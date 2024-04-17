#nomes = ['Felipe', 'Daniel']  Pode ser atribuído com os colchetes ou como list(), pode ser armazenado qualquer tipo de dado (bolean, int, float)
#print(nomes[1]) o tipo de dado que for puxado irá retornar como list

'''
Para manipular os dados
É possível várias informações em uma única só váriavel

As informações possuem um index, quando possue alguma ordem


Cada variavel tem uma ordem e dessa ordem é iniciada com 0 e vai aumentando de 1 em 1

Se for printado apenas a váriavel vai com todos os dados dentro do colchetes, para imprimir um dado específico, basta colocar o index dele dentro do colchetes

Qualquer elemento dentro da lista pode ser modificado, pode ser alterado

Os dados podem ser misturados

nomes = ['Felipe', 'Daniel', 'Joao', 'Douglas']
#Se quiser alterar um único valor
nomes [0] = "Felipe Verde"
#nomes.append('Felipe') #Adiciona um elemento na lista no final
print(nomes)

#Tem como misturar lista com laços de repetição

nomes = []

while True:
    nome = input('Digite -1 para sair ou cadastre um nome: ')
    if nome == '-1': #Se o nome for -1 ele vai sair do laço
        break

    nomes.append(nome) #Se o nome for diferente de -1 ele vai ser adicionado na lista e assim que for digitado -1 ele vai sair do laço e vai aparecer todos os nomes digitados

print(nomes)

'''

 # Não é permitido utilizar métodos como reverse ou sort.

"""lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)
print(lista_invertida)
[{1}, 5, "a"]"""

lista = ['a', 5, {1}]

for elemento in lista[::-1]: # o [::-1] é o operador de fatias, permite criar uma nova lista com elementos da lista original e fazer a ordem inversa
    print(elemento)


