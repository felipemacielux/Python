#Escreva um programa onde o usuário digite duas notas e ele mostre a média das duas notas

nota1 = input("Digite a sua primeira nota: ")
nota2 = input("Digite a sua segunda nota: ")
nota1 = int(nota1)
nota2 = int(nota2)

''' No entanto para o código ficar mais organizado precisaria ser feito
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

print ('Sua média final é (media)')

'''

print(f"A sua média final é: {(nota1 + nota2) / 2}")