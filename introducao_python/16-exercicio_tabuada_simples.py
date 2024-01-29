# Receba um número do usuário e mostra a tabuada desse número


n1 = int(input("Digite um número que deseja saber a tabuada: "))

i = 1
while i <= 10:
    print(f"{n1} x {i} == {n1*i}")
    i += 1