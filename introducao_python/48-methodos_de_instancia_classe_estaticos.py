class Evento: # classe em python que define como criar os objetos
    def metodo_instancia(self): # self representa a própria instancia da classe
        return("método de instância chamado", self)
    
    @classmethod # decorador que indicará que o metodo seguinte é um metodo de classe
    def metodo_classe(cls): # o cls serve para referenciar a propria classe, definido como cls
        return("metodo de classe chamado", cls)
    
    @staticmethod # decorador que indica que o metodo seguinte é estastico, são funções que não dependem de instancias e nem de classes, não recebe nenhum argumento
    def metodo_estatico():
        return "estatico chamado"
    

ev = Evento()
a = ev.metodo_instancia() # o que está acontecendo nessa linha é que está passando Evento.metodo_instancia(ev), fazendo a chamada a partir de um objeto, e esse objeto é passado como parametro self
print(a)

b = Evento.metodo_classe() # Vai chamar o Evento e passar a referência da classe para esse metodo Evento.metodo_classe(Evento)
print(b)

c = Evento.metodo_estatico()  