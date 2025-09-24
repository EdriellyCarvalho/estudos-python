#Exercício: Dobrar valores da lista 
#Dada uma lista de inteiros, retorne uma nova lista com os valores dobrados.

def dobrar_valores(lista):
    return [x * 2 for x in lista]
#Teste
lista = [3, 4, 9, 10]
print(dobrar_valores(lista))