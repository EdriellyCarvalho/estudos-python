#Exercício: Divisão segura
#Leia dois números e faça a divisão.
#Se o usuário tentar dividir por zero, exiba uma mensagem de erro.

try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida")
except ValueError:
    print("Erro: Entrada inválida, por favor insira apenas números inteiros")
print("\nFim do programa")