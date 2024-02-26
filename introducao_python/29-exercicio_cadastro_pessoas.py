#Faça um programa que o usuário possa cadastrar n pessoas, armazenando seu nome idade, altura

pessoas = [] # Essa lista vazia serve para armazenar os dados que serão cadastrados pelo usuário

while True: # inicia um loop infinito que repetirá até que seja interompido com o break, aqui pode ser colocada todas as informações que o usuário deseja cadastrar
    pessoa = {} # Cria dicionário para conter as informações de cada pessoa (nome, idade, altura)
    pessoa['nome'] = input('Cadastre um nome: ')
    pessoa['idade'] = int(input('Cadastre uma idade: '))
    pessoa['altura'] = float(input('Cadastre uma altura: '))
    if input('Quer continuar? [S/N] ').upper() == 'N': # upper deixa todas as letras maiúsculas independente se o usuário digitar minúsculo ou maiúsculo
        break
    pessoas.append(pessoa) # Após obter todas as informações, adiciona o dicionário na lista usando o metodo append


    print(pessoas)