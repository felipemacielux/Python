'''
Diferença entre o laço for e laço while

while -> Tudo que for fazer com laço for tem como fazer com laço while
Utilizado quando você não sabe quantas vezes seu laço irá rodar
for -> Possui algumas limitações



for i in range(0, 5): #para i em um intervalo de 0 a 5 (mas o 5 não entra e ele iria até o 4) ele vai até o valor -1
    print(i)
'''
#Senão quiser que chega de um número a tal número muito grande, o ideal é trabalhar com intervalos, esses intervalos para pular de 2 em 2 e assim por diante são nomeados como step, e são colocados na "terceira" casa

for i in range(0, 100, 2): #Aqui nesse caso ele está indo de 2 em 2, definindo um intervalo de tempo
    print(i)

'''
Para ordem decrescente:

for i in range(100, 0, -1): 
    print(i)

Tem que ser ao inverso

print(list( range(100, 0, -1) ))

iterando

Da para percorrer mesmo sendo caracter (string)


'''

x = input("Digite seu nome: ")

for i in x:
    print(i)
