# Tem como importar o que está destacado no arquivo minha_lib

#import minha_lib

#print(minha_lib.x)  quando for executado esse código python vai mostrar o valor de x = 10

#Quando precisar só importar um valor especifico

#from minha_lib import x 
# quando for executado esse código python vai mostrar o valor de x = 10

# Quando quiser importar tudo dentro de uma biblioteca basta colocar *

#from minha_lib import *

# Se for utilizado precisar ser importado a váriavel de outro arquivo e precisar colocar uma váriavel com o mesmo nome deve ser feito

'''
from minha_lib import x as x_importado
 
x = 50

print(x)
print(x_importado)

Vai aparecer ambas as váriaveis


'''

from minha_lib import soma_numeros #Tem como importar uma função especifica do arquivo

x = soma_numeros(10, 5)

print(x)