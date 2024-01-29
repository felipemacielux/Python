#Mostra a tabuada completa de todos os números entre 1 e 10

for i in range (1, 11): #Variavel i vai representar em qual váriavel você se encontra, representa o número que supostamente seria digitado pelo usuário
    print(f"=======[TABUADA {i}]=======")
    # A váriavel j representa o número na qual aquela tabuada está sendo multiplicada
    for j in range(1, 11):
        print(f"{i} X {j} == {i*j}")