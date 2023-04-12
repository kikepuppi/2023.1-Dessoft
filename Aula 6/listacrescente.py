# lista crescente
lista = [0,2,7,1,0,45]
def estritamente_crescente(lista):
    lista2 = []
    y = 0
    for x in range(len(lista)):
        if x == 0:
            lista2.append(lista[x])
        if lista[x] >= lista[0]:
            if lista[x] > lista2[y]:
                lista2.append(lista[x])
                y += 1
    return lista2
print(estritamente_crescente(lista))
