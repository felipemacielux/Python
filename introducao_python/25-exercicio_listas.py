# Receba 10 valores e exiba a soma de todos eles

idade = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
'''
Ou pode ser feito dessa forma:

x = [int(input("Digite um valor: ")) for i in range(0, 10)] # Cria uma lista chamada x que é preenchida com 10 valores inseridos pelo usuário

soma = 0
for i in x:
    soma += i
print(soma)

'''
soma = 0 # Variavel utilizada para acumular a soma dos valores da lista
for i in idade: # Loop for que percorre cada elemento da lista idade/iniciando na posição zero que o valor será o primeiro
    soma += i # O valor atual de i é somado a variavel soma e isso será para acumular todos os elementos da lista
print(soma)
