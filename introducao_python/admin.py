from ex_classes import Usuario

class Administrador(Usuario):
    def imprime_usuario(self):
        return super().imprime_usuario() # o super no codigo faz com que chama explicitamente o metodo imprime_usuario da classe base Usuario