#Escreva um programa que receba notas de um aluno (0 - 10), caso a nota digitada esteja fora dessa intervalo peça para o professor digitar novamente

while True:
    nota_aluno = int(input("Digite a nota do aluno: ")) #Isso faz com que fique pedindo para que a nota do aluno seja digitada, até que digite uma nota válida, interrompe o laço e da o prosseguimento
    if nota_aluno >= 0 and nota_aluno <= 10: # Vai validar se é um o outro é true para ler a condição do if
        print(f"Nota armazenada com sucesso {nota_aluno}") 
        break
    else:
        print('Nota inválida, digite novamente')# Não precisa do else e se sair do laço não será necessário executar essa linha novamente