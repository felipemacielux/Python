#Variaveis e tipos de dados

# 1° receber dados
# 2° armazenar dados
# 3° Processar dados
# 4° Mostrar dados processados


# int (inteiro)
# float(decimal)
# string (cadeia de caracteres)
#boolean (true/false)

idade = 21 #nome que daremos ao dado que vai ser armazenado na memória RAM o = é utilizado para atribuição e depois dele vem o dado que vai responder ao dado armazenado (ex: quando chamar idade, ela será igual a 21).
print(type(idade))

#COnforme os valores forem colocados em ordem como:
#idade = 21 
#idade = 22
# e dar um print o valor será sobreescrito em relação ao primeiro

#Conceito de variaveis como constante é feita com a letra maiscula, ex:
#IDADE = 20 diferente de idade = 20


#EXERCICIO

valor_compras = 50.70
desconto = 0.05

quantidade_itens = 3

total_das_compras = 50.70 - (50.70 * 0.05)

print(int(total_das_compras)) # colocando para imprimir apenas o valor inteiro por mais que de decimal

custo_medio = total_das_compras // quantidade_itens # nesse caso o // vai arredondar para baixo
print(custo_medio)