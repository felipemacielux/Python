'''
import os #importa o modulo de funções para interagir com o sistema operacional


x = lambda: os.system('clear') #função lambda não aceita nenhum argumento e retorna o sistema operacional para limpar a tela

'''

x = lambda nome, idade: print(f'{nome} tem {idade} anos') #usando a função lambda atribuindo a váriavel x com os parametros idade e nome

x('Felipe', 21) #estamos chamando a função lambda e atribuindo os valores Felipe e 21 para os parametros nome e idade