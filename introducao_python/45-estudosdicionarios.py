# Em dicionarios é possível acessar itens, remover, juntar os dicionarios


#Escreva um programa Python que conte a frequência de cada letra em uma string


string = "exemplo de string" #Definindo uma string para analisar e contar a frequência
frequencia = {} #Definindo um dicionário para armazenar a frequência
for letra in string: # inicia um loop para percorrer cada letra da string
    if letra.isalpha():  # Verifica se é uma letra
        # O método isalpha() retorna True se o caractere for uma letra e False caso contrário.
        letra = letra.lower()  # Converte para minúscula
        frequencia[letra] = frequencia.get(letra, 0) + 1
print(frequencia) 