'''
Precisa exibir um bloco de código e executar um determinado bloco de código em alguma quantidade de vezes

o While executa o código mais de uma vez

Também tem condições assim como if elif else

while -> significa enquanto

ex: enquanto (while) a condição for verdadeira executa o bloco de código



i = 0
while i < 5:
    print('Olá, tudo bem?')
    print('Como vai você?')
    i += 1 # Como se fosse um incremento i = i + 1

# O código acima vai rodar 5 vezes, porque ele vai pegar sempre o resultado somar com 1 (incremento) voltar para a linha 14



usuario = "Felipe" 
senha = "123456"

while True:

    nome_usuario = input("Digite o nome de usuário: ")
    senha_usuario = input("Digite a senha: ")

    if nome_usuario == usuario and senha_usuario == senha:
        print("Autenticação foi bem sucedida.")
        break
    else:
       print("Usuário ou senha inválido.")
        

    # na estrutura do código sempre colocar primeiro as váriaveis que serão armezenadas no inicio do código
    #abrindo o laço de repetição, colocar o que o usuário vai inserir nos campos solicitados
    # e sobre ela abrir as condicionais se necessário

    '''
"""
n1 = int(input("Digite um número: ")) # recebendo o número do usuário

i = n1 # iniciando do número que o usuário digitou
while i <= 100: # enquanto o número for menor ou igual a 100
    print(f"Lista de {n1} a 100: ", i) # exibindo os números do usuário a 100
    i += 1 # vai somando mais um enquanto o looping for true

print("Fim")

"""
'''

n1 = int(input("Digite um número: ")) 

i = n1
while i <= 100: # Aqui abre o laço de repetição que enquanto o número digitado pelo usuário for menor ou igual a 100
    if i % 2 == 0: # abre uma condincional que enquanto o número digitado pelo usuário for divisível por 2 e o resto for igual a 0
        print(f"Números pares de {n1} a 100: ", i) # vai ser exibido os números pares
    i += 1 # vai somando mais um enquanto o looping for true

print("Fim")


'''
'''

n1 = int(input("Digite um número: ")) # está recebendo o número do usuário

if n1 < 2: # verificando se o número digitado pelo usuário é menor que 2 (abrindo a condicional)
    print("O número não é primo.") # se o número for menor que 2 vai exibir essa mensagem
else: # se o número for maior que 2 entra no bloco de código abaixo
    i = 2 # iniciando do 2 e será utilizada para verificar se o número é divisível por outros números
    while i * i <= n1: # esse laço continuará executando enquanto i^2 for menor ou igual ao número digitado
        if n1 % i == 0: # aqui vericamos se o número digitado pelo usuário é divisível por i
            print("O número não é primo.") # se for divisível vai exibir essa mensagem e sai do laço com o break abaixo
            break
        i += 1
    else:
        print("O número é primo.")

print("Fim")
'''
#Jogo Acerte o número   

n1 = 8 # armazenado a váriavel que o usuário terá de acertar
tentativas_max = 3 # armazenado a quantidade de tentativas maximas
tentativas = 0 # iniciando o contador de tentativas

while tentativas < tentativas_max: # inicia o laço de repetição
    n2 = int(input("Digite um número: "))
    if n2 == n1: # se o número digitado pelo usuário for igual a n1
        print("Parabéns, acertou!")
        break
    elif n2 > n1: # se o número digitado pelo usuário for maior que n1
        print("Tente um número menor!")
    elif n2 < n1: # se o número digitado pelo usuário for menor que n1
        print("Tente um número maior!")
    
    tentativas += 1 # vai somando os números de tentativas caso o usuário erre 
else:
     print("Tente novamente!") # Fugindo da identação para ser executado assim que o número de tentativas_max for atingido