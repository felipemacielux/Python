# Receba uma temperatura em farenheit e exiba em graus celsius.

''' Para converter uma temperatura 

c = 5 * f - 32/9 -> formula para calcular a temperatura em graus celsius tendo como base a temperatura farenheit






'''

temperatura_farenheit = float(input('Digite uma temperatura em graus farenheit: '))

temperatura_celsius = 5 * ((temperatura_farenheit - 32)/9)

print(f'A temperatura em graus celsius é de {temperatura_celsius}')  