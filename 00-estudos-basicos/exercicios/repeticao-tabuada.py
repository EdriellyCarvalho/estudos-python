#Exercício: Tabuada
#Escreva um programa que exiba a tabuada de um número fornecido pelo usuário.

n = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")