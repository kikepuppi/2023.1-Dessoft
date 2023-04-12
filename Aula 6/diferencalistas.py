# diferenca de lista
lista1 = [2, 7, 3.1, 'banana']
lista2 = [2, 'banana', 'carro']
def subtracao_de_listas(lista1, lista2):
    lista = []
    for x in range (len(lista1)):
        if lista1[x] not in lista2:
            lista.append(lista1[x])
    return lista

print(subtracao_de_listas(lista1, lista2))