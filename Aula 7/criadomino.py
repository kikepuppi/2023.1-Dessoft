# cria peças de domino
import random as rd
def cria_pecas():
    lista = []
    for i in range(0,7):
        for j in range(0,7):
            listapequena = [i,j]
            if [i,j] not in lista and [j,i] not in lista:
                lista.append(listapequena)
    rd.shuffle(lista)
    return lista

print(cria_pecas())
