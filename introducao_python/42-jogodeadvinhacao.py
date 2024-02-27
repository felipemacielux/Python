#Primeiro deve ser feito a importação do modulo

import random #importação de modulo para gerar números aleatórios

# Geração do número secreto

secret_number = random.randint(1, 100)# Gera um número aleatório entre 1 e 100

# Inicialização de Variaveis

guess = 0 # variavel que será armazenada a tentativa do usuário
attempts = 0 # variavel que vai contar as tentativas

print("Advinhe o número que estou pensando entre 1 e 100")

#Inicio do loop while

while guess != secret_number:# loop que vai continuar a ser executado enquanto o valor da variável guess for diferente do valor da variável secret_number
    attempts = attempts + 1 # vai incrementando 1 a cada vez que o loop for executado
    guess = int(input("Tente adivinhar: "))# faz com que o usuário insira um número inteiro

# Verificação de tentativas

    if guess > secret_number: # Se a tentativa do jogador for maior que o número secreto, imprime uma mensagem indicando isso.
        print("O número que eu estou pensando é menor que isso")
    elif guess < secret_number: # Se a tentativa do jogador for menor que o número secreto, imprime uma mensagem indicando isso.
        print("O número que eu estou pensando é maior que isso")
    else:  # Se nenhuma das condições anteriores for verdadeira, significa que o jogador acertou o número secreto e uma mensagem de parabéns é impressa
        print("Parabéns, voce acertou o número em", attempts, "tentativas")