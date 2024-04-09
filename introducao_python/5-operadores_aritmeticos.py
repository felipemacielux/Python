''' os operadores são
 + soma
   - subtração
     / divisão
       * multiplicação
         ** exponenciação
           % - modulo (resto de uma divisão inteira)
             // divisão por inteiro (não aceita que o resultado da divisão seja um ponto flutuante)
               math.sqrt (raiz quadrada)
'''               

#Para usar a raiz quadrada precisa primeiro ser importado a biblioteca para uso
'''import math


operacoes = math.sqrt(4)

print (operacoes)
 
 # O () na operação abre a prioridade de ser executado primeiro

#EXERCICIO

n1 = int(input('Digite um número: '))

if n1 % 2 == 0:
    print('par')
else:
    print('impar')

resultado = ((2 + 3) * 2) ** 2
print(resultado)
'''

val_compra = float(input("Digite o valor da compra: "))
val_frete = float(input("Digite o valor do frete: "))
cliente = input("Cliente é cadastrado no programa de fidelidade? s (SIM) ou n (NÃO): ")
if val_compra + val_frete > 100 and cliente == 's':
    print('O cumpom pode ser utilizado.')

else:
    print('O cumpo não pode ser utilizado.')