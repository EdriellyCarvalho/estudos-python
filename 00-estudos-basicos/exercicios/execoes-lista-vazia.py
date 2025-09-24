#Exercício: Lista vazia
#Tente calcular a média dos valores de uma lista. Se a lista estiver vazia, trate a exceção corretamente.

def media(lista):
    try:
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        return "Erro: não é possível calcular a média de uma lista vazia."
#Teste:
print(media([6, 8, 10]))
print()
print(media([]))
