# Porque quando uma lista é igual a outra temos a mesma lista

x = 2
y = x

print(id(x)) # printa o endereço de memória de onde a váriavel está
print(id(y))

# O endereço de memória de x e o endereço de memória de y se repete, ou seja, temos a mesma lista, agora se utilizar o .copy ele vai criar uma nova lista e não vai usar o mesmo endereço de memória