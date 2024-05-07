'''d = {"a": 1}

d.keys() # d se refere ao dicionário que é um tipo e d é um objeto desse tipo de dicionario

Nas classes, mesmo criando uma nova váriavel com os mesmos atributos e váriavel diferente, será objetos diferentes


class Evento: # classe que representa um tipo de objeto que será declarado depois os atributos e metodos relacionados ao evento
    # Caso seja preciso que o atributo seja alterado
    def altera_nome_evento(self, novo_nome): # primeiro argumento sempre será referência do objeto (self)
        print("Alterando nome do evento")
        self.nome = novo_nome

ev = Evento()# semelhante a chamada de função, mas estamos chamando a classe, fazendo com que um novo objeto seja criado em nossa memória
# Adicionar tributos dinamicamente
# ev aqui é como se fosse a instância da classe Evento
ev.nome = "Aula"
print(ev.nome)

# Quando é feito obj.metodo => logo ele chama o Evento.metodo.obj (o interpretador vai passar o próprio objeto como referência, como primeiro argumento da função)

ev.altera_nome_evento("Aula 2") # precisa do ev para chamar objeto do nosso evento e o metodo vem depois, não precisando passar o objeto nos argumentos
print(ev.nome) 



# Uso do construtor __init__ 

class Evento: #classe que representa um tipo de objeto que será declarado depois os atributos e metodos relacionados ao evento  
    #metodo especial no python (construtor), é feito com a intenção de inicialiação do objeto
    def __init__(self, nome): #Primeiro argumento novamente tem de ser o self, e depois todos os argumento que deseja você forçar o seu objeto a ter
        # Pode ser adicionados atributos normalmente
        self.nome = nome # mesmo nome de atributo que foi passado nos argumentos
        self.local = "Brasil"

    def altera_nome_evento(self, novo_nome): # primeiro argumento sempre será referência do objeto (self)
        print("Alterando nome do evento")
        self.nome = novo_nome

ev = Evento("Trabalho presencial")
ev2 = Evento("Trabalho remoto")

print(ev.nome) # Será impresso porque a função com o metodo construtor foi forçado
print(ev.local)
print(ev2.nome)
print(ev2.local)

'''
class Car: # Criação da classe
    def __init__(self, make, model, year): # Criação do metodo construtor para que seja chamada nas demais funções, passando assim também os parametros para tranformar em atributos 
        self.make = make
        self.model = model
        self.year = year

    def start(self): # Criando um metodo colocando como argumento self para pegar os parametros 
        print(f"Starting {self.make} {self.model} {self.year}") # pegando os atributos

    def stop(self): 
        print(f"Stopping {self.make} {self.model} {self.year}")

car = Car("Toyota", "Corolla", 2022) # passando os valores para o construtor da classe Car, que inicializou com os atributos make, model, year

car.start()
car.stop()