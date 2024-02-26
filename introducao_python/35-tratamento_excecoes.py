#permite que você lide com erros que podem ocorrer durante a execução do seu código de forma controlada, não permitindo que o código seja interrompido por erros de sintaxe ou de logica.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

try:
    print(n1/n2)

except:
    print('Ocorreu um erro!') # como se fosse if/else, ao invés de mostrar o erro que da no console vai mostrar o que estiver dentro do except

finally:
    print('Fim do programa')# sempre será executado no try ou no except

