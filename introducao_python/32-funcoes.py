#Função é uma estrutura que pode ou não receber dados e pode ou não retornar dados, processar alguma informação e executar uma ação
'''
def minha_funcao():
    print('Oi')
    print('Tchau') #senão chamar a função logo abaixo, ele não vai ser executado e não vai mostrar o valor

minha_funcao()# Pode ser chamada quando quiser e quantas vezes quiser'''

def minha_funcao():
    soma = 0
    for i in range(0, 20):
        soma += i
    print(soma)

minha_funcao()