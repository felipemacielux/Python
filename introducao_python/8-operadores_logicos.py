'''
Assim como os operadores relacionais os operadores logicos sempre vão retornar se o dado é false ou true
and e = só retorna true se o dado da direita e da esquerda for verdadeiro, se um dos lados for false irá retornar com false
or ou = basta se um dos lados forem true, irá retornar com true
not não = se algum dado for verdadeiro ele transforma em falso e se tiver algum falso ele transforma em verdadeiro 




'''

operador = False and False 

print(operador)

idade = 16
maioridade = idade >= 18
maioridade = not maioridade

print(maioridade)


a = 5
b = 10
x = True
y = False

print((x or y) and (a < b))
print((x or y) and not (a < b))



