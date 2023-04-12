# sorteador de numeros bingo

import random as rd
n = 4
lista = [10, 1, 5, 6, 9, 15, 2]
def distribuir(n, lista):
    lista2 = []
    l = len(lista)
    for x in range (n):
        a = (rd.choice(lista))
        while a in lista2:
            a = (rd.choice(lista))
        lista2.append(a)
    return lista2
print(distribuir(n,lista))