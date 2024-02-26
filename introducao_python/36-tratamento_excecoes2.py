#tratamento de exceções


try:#usado para envolver o bloco de código que pode gerar um erro
    x = int(input('Digite um número: '))
    print (5/x) #vai pegar o número digitado pelo usuário e dividir por 5
except ValueError:#irá ser executado se o usuário digitar um valor que não seja um número
    print ("Digite um número inteiro")
except ZeroDivisionError:# será apresentada se o usuário digitar 0
    print ("Impossível dividir por zero")