#Defina um usuário e senha e depois verifique se login do usuário é válido

usuario = "Felipe"
senha = "minhasenha123"

#Objetivo aqui é fazer com que o usuário faça a tentativa de colocar o login e validar se colocou correto ou não 

while True:
    usuario_login = input('Digite seu nome de usuário: ')
    senha_login = input('Digite sua senha: ')

#Agora vamos validar se as duas váriaveis da linha 3 e 4 coincidem com as da linhas 9 e 10
    if usuario_login == usuario and senha_login == senha:
        print('Você foi logado no sistema!')
        break
    else:
        print('Usuário e senha inválido.')