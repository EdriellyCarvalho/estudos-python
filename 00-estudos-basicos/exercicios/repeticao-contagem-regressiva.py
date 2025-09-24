#Exercício: Contagem REgressiva
#Peça ao usuário um número N e exiba a contagem regressiva até 0.

n = int(input("Digite um número para iniciar a contagem regressiva: "))
for i in range(n, -1, -1):
    print(i, end=' ')
