'''

Ferramenta de debug

Quando chegar em certa linha do código ele vai pausar e aos poucos vai mostrando o que está executando


Debug é a ferramenta acima das extensões do vscode, ela consegue filtrar linha por linha como o código pode ser executado aos poucos


i = 0
j = 0
while i < 10 and j < 30:
    print('Olá, tudo bem?')
    print('Como vai você?')
    i += 1 # Como se fosse um incremento i = i + 1
    j += 10

É possível parar o código com break do próprio while, que acaba saindo do laço de repetição


while i < 10:
    print(i)
    break # interrompe o laço de repetição mesmo que a condição seja verdadeira 
    i += 1


    i = 0

while i < 10:
    print(i)
    if i >= 5:
        break
    i += 1


'''
i = 0

while i < 10:
    print(i)
    if i % 2 == 1:
        i = i + 2
        continue
    i += 1