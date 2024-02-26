'''# Como criar chaves que ainda não foram pré definidas em um determinado dicionário

pessoa = {'nome': 'Felipe', 'idade': 25, 'altura': 1.80}

pessoa['cep'] = '12345-678'# não vai dar erro, vai criar uma nova chave
# ou pode ser feito dessa forma com update
pessoa.update({'cep': '12345-678'}) # vai atualizar o dicionário


print(pessoa)'''


# Se quiser apenas as chaves dos dicionários ou apenas os valores do dicionário


pessoa = {'nome': 'Felipe', 'idade': 25, 'altura': 1.80}

print(pessoa.keys()) # vai mostrar as chaves
print(pessoa.values()) # vai mostrar os valores

# se for feita a iteração

for i in pessoa.items(): # se fpsse puxar sem items, vai mostrar apenas as chaves, agora com mostra os valores e as chaves
    print(i)