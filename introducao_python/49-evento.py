class Evento:
    def __init__(self, nome, local = ""): #Argumentos com valor padrão e todo local se não for passado vai assumir o valor de uma string vazia
        self.nome = nome
        self.local = local 
       # Criar um metodo de instancia só imprime informações do evento 
    def imprime_informacoes(self): # Instancia da classe evento
        print("Nome do evento: ", self.nome)
        print("Local do evento: ", self.local)

    @classmethod
    def cria_evento_online(cls, nome): # fazendo referencia a classe Evento do inicio do codigo
        evento = cls(nome, local = "https://tamarcado.com/eventos?id=1")
        return evento
    
    @staticmethod # não depende da classe e nem da instancia, mas pode receber argumentos
    # Objetivo: Calcula o limite de pessoas que pode ter baseando-se em uma metragem
    def calcula_limite_pessoas(area):
        if area >= 5 and area < 10: # 5 <= area < 10 -----> fica mais legível assim no código
            return 5
        elif area >= 10 and area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0
        

# Sendo criado a classe ev_online, que é uma instância da classe Evento
ev_online = Evento.cria_evento_online("Live Sobre") # recebe o interpretador por debaixo dos panos
ev_online.imprime_informacoes()

print(Evento.calcula_limite_pessoas(18)) # metodo estatico sendo chamado







'''ev = Evento("Liquidação de ofertas") Fazendo com que execute apenas a linha de baixo ev2 que contém ambas as informações para serem preenchidas conforme a função imprime_informacoes
ev2 = Evento("Liquidação de ofertas", "Franca, São paulo")

ev2.imprime_informacoes()'''

