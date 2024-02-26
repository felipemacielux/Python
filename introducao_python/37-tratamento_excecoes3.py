#Como verificar qual foi a exceção que ocorreu no código


try:
    x = int(input('Digite um número: '))
    print (5/x) 
except Exception as e:# Utilize essa modularização como e
    print (e) #está capturando qual exceção ocorreu