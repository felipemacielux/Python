x = [i for i in range(0, 10)] # Para cada valor de i dentro do escopo númerico, adicione i dentro da lista

y = []
for i in range(0, 10):
    y.append(i)

print(x)
print(y)

# O metodo do x é bem mais rapido que o do y, mais eficiente

z = [i*2 for i in range(0, 10)] # Aqui a cada elemento da lista sendo ela de 0 até 10 vai ser multiplicado por 2

print(z)

# ou dessa forma, que ressalta a lista primeiro e só coloca o nome da váriavel

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i*2 for i in a]

print(b)

# Tem como adicionar listas dentro de lista com o list comprehension

c = [ [j for j in range(4,7) ] for i in range(0,3)]

print(c)


# Tem como colocar as listas junto com as condições

z = [i for i in range (0,10) if i > 4] # Aqui vai retornar todos os valores maiores que 4

print(z)