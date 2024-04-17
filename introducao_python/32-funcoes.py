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
é o valor desse número.'''

def maior_num(numeros): # definindo a função que recebe como argumento numeros 
    pos = 0 # Esta variável será usada para armazenar a posição do maior número na lista.
    num = 0 # Esta variável será usada para armazenar o maior número encontrado até o momento durante a iteração pela lista.
    for i in range(len(numeros)): # Inicia o loop onde percorre os indices de numeros e retorno o comprimento da lista/numero total de elementos
        if numeros[i] > num: #verificar seo numero atual na posição i é maior que o num
            num = numeros[i] #verifica se o número atual da posição i for maior que o num, atualia o valor de num na atual posição i
            pos = i # atualiza o valor de pos na atual posição i, indicando a posição do maior número na lista
    return (pos, num)