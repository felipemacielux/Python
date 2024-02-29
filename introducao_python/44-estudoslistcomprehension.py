# Dobrando o valor de um produto

precos = [int(input("Precos:")) for i in range(0, 10)] # Cria uma lista de precos

novo_precos = [] # lista vazia
for preco in precos: # laço de repeticão em que vai percorrer toda a lista iterar e depois multiplicar por 2 com o metodo abaixo
    novo_precos.append(preco*2)

print(novo_precos)


#agora com o list comprehension
novo_precos2 = [preco*2 for preco in precos]
print(novo_precos2)

# OU

# Solicita ao usuário inserir os preços e cria uma lista de preços
precos = [int(input("Preço: ")) for _ in range(10)]

# Lista comprehension para multiplicar cada preço por 2
novo_precos = [preco * 2 for preco in precos]

# Imprime a lista de preços modificada
print(novo_precos)
