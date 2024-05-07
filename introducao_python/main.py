# A estrutura ficará da seguinte forma
# 1° Vai ser a ex_classes --> admin --> main (na main importando ambas e na admin apenas o ex_classes)


from ex_classes import Usuario 
from admin import Administrador

# Exemplo de uso
usuario1 = Usuario("Gabriel", "gabriel@exemplo.com")
usuario2 = Administrador("Lucas", "lucas@exemplo.com")

usuario1.imprime_usuario()  # Saída: Gabriel (gabriel@exemplo.com)
usuario2.imprime_usuario()  # Saída: Lucas (lucas@exemplo.com) – Administrador

print(f"Quantidade total de instâncias: {Usuario.quantidade}")
