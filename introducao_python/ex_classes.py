# Criação da classe
class Usuario:
    quantidade = 0 # Atributo de classe para contar as intancias

#Criação do metodo construtor
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.quantidade += 1 # Vai incrementar a quantidade de instâncias dependendo de quantas vezes o objeto for chamado

#Criação do metodo de instancia
    def imprime_usuario(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")



