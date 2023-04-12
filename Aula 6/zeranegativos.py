# substitui negativos por zero

lista = [0,-1,-2,4,5,6,7,-8]
def zera_negativos(lista):
    x = 0
    for x in range (len(lista)):
        if lista[x] < 0:
            lista[x] = 0
        x += 1
    return lista

print(zera_negativos(lista))