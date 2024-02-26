'''raise ValueError("Invalid value") Pode ser qualquer tipo de exceção desde que exista
 '''


def soma(n1, n2): # define uma função que recebe dois números como argumentos
    if n1 < 0 or n2 < 0:
        raise ValueError("Invalid value") # se as condicoes forem atendidas, o erro vai ser disparado
    return n1 + n2

print(soma(1, -2)) 


x = -1
assert x > 0, "Invalid value" # estamos definindo que o assert seja forçado que algo seja verdadeiro(para fazer a verificação se é verdadeiro ou falso)