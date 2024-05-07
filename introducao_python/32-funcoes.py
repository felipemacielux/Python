#Função é uma estrutura que pode ou não receber dados e pode ou não retornar dados, processar alguma informação e executar uma ação
'''
def minha_funcao():
    print('Oi')
    print('Tchau') #senão chamar a função logo abaixo, ele não vai ser executado e não vai mostrar o valor

minha_funcao()# Pode ser chamada quando quiser e quantas vezes quiser

def minha_funcao():
    soma = 0
    for i in range(0, 20):
        soma += i

minha_funcao()

# para as palavras utilizadas quando é definida uma função ela vai obedecer a ordem de como está escrita

def dar_boas_vindas(nome, sobrenome, nome_do_curso):
    print("Olá, ", nome, sobrenome)
    print("Bem vindo ao curso de ", nome_do_curso)

dar_boas_vindas(nome = "Felipe", sobrenome="Maciel", nome_do_curso="ADS") # mesmo se trocar a ordem de como vai ficar, ele vai obedecer de acordo como está o print, mesmo que não for preciso utilizar os argumentos nomeados ele vai entender para onde o argumento vai ao ser impresso




def calcular_conta(consumo, taxa_de_servico, desconto_fidelidade): # Se os valores forem passados aqui serão valores padrão
    servico = consumo * taxa_de_servico
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    print("O valor a ser pago é:", valor)
    #ou por ser feito com return
    #return valor
#valor = calcular_conta (consumo=100, taxa_de_servico=0.1, desconto_fidelidade=0.05)
calcular_conta (consumo=100, taxa_de_servico=0.1, desconto_fidelidade=0.05) # diferente dos valores padrão aqui são os keywords


consumo = 100
servico = consumo * taxa_de_servico
desconto = consumo * desconto_fidelidade


valor = consumo + serviço
valor = valor - desconto





number = int(input("Digite um número inteiro: "))

if number > 1: # Aqui vai validar se o número é maior que um, porque os números primos começam a partir do dois
    for i in range(2, number): # vai verificar se o número entre 2 e o digitado pelo usuário
        if number % i == 0: # se for divisivel por i não é primo
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo') # senão ele é primo
elif number == 0:
    print(number, 'é zero')
elif number == 1:
    print(number, 'é um')
else:
    print(number, 'é negativo')

'''




'''
    
def solicitar_dado():
    dado = int(input("Por favor, digite um número para verificar se é primo ou não: "))
    
    if dado <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    
    for i in range(2, int(dado ** 0.5) + 1): # vai percorrer todos os números a partir 2 até a raiz do número inserido pelo usuário e arrendonda somando mais um
        if dado % i == 0:
            return False  # Se for divisível por algum número além de 1 e ele mesmo, não é primo
    
    return True  # Se não for divisível por nenhum número além de 1 e ele mesmo, é primo

# Chamando a função e imprimindo o resultado
print(solicitar_dado())

Implemente uma função que recebe uma lista de números inteiros e retorna uma
tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num
é o valor desse número.


def maior_num(numeros): # definindo a função que recebe como argumento numeros 
    pos = 0 # Esta variável será usada para armazenar a posição do maior número na lista.
    num = 0 # Esta variável será usada para armazenar o maior número encontrado até o momento durante a iteração pela lista.
    for i in range(len(numeros)): # Inicia o loop onde percorre os indices de numeros e retorno o comprimento da lista/numero total de elementos
        if numeros[i] > num: #verificar seo numero atual na posição i é maior que o num
            num = numeros[i] #verifica se o número atual da posição i for maior que o num, atualia o valor de num na atual posição i
            pos = i # atualiza o valor de pos na atual posição i, indicando a posição do maior número na lista
    return (pos, num)
# Solicitar que o usuário insira a lista de números
entrada = input("Insira a lista de números separados por espaços: ")

# Convertendo a entrada do usuário em uma lista de inteiros
numeros = [int(x) for x in entrada.split()] # o metodo split() divide a string em substrings, ele irá dividir a string onde encontrar espaços em branco, então se o usuário digitar 10 20 30, ele vai entender como [10, 20, 30]
# o int(x) está transformando a lista em números inteiros
# Fazendo com que ocorra da seguinte forma: Para cada elemento x na lista resultante de entrada.split(), converta x em um número inteiro e adicione-o à lista numeros

# Chamando a função e imprimindo o resultado
resultado = maior_num(numeros)
print("O maior número é:", resultado[1], "na posição:", resultado[0])



pessoa = (input("Nome: "), int(input("Idade: "))) # Tupla contendo o nome e a idade que solicita o usuário

def maior_idade(pessoa): # definindo a função maior_idade que recebe como argumento pessoa
    nome, idade = pessoa # devem ser identifcadas as váriaveis para que possa se referir a pessoas
    if idade >= 18: # fazendo a verificação
        return True
    else:
        return False

resultado = maior_idade(pessoa) # aqui deve ser chamado a função
print(resultado) # aqui impresso o resultado dela, se é true ou false
    

pessoa = {} # aqui já criamos um dicionário vazio, para que seja armazenado nele os dados de nome e idade

nome = input('Nome: ') 
idade = int(input('Idade: '))

def maior_idade (pessoa): # definindo a mesma função que anteriormente
    pessoa['nome'] = nome # identificando nome e idade que foi solicitado para o usuário
    pessoa['idade'] = idade
    if pessoa['idade'] >= 18: # validando entre true ou false
        return True
    else:
        return False
    

print(maior_idade(pessoa)) # chamando a função para apresentar os resultados
   
    
'''
def check_element(lista, elemento): # definindo a função check_element
    for item in lista:  # aqui vai percorrer cada item da lista
        if item == elemento: # verifica se o elemento atual é igual ao elemento procurado
            return True
    return False

# Exemplo de uso da função 
lista_exemplo = [1, 2, 3, 4, 5]
elemento = int(input("Digite um número para descobrir se está na lista: "))

print(check_element(lista_exemplo, elemento))  # Saída: True
