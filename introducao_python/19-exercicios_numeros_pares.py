#Receba um numero e mostre todos os numeros pares de 0 até o n° digitado

'''
O intuito é mostrar todos os números pares entre 0 e 1000 




'''

n1 = int(input("Digite um numero: "))


i = 1
while i <= n1:
    if i % 2 == 0: #mod = se a variavel i dividida por 2 se o resto da divisão dela for igual a zero, o resultado deve ser um número par

        print(i)
    i += 1

    