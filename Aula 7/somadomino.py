# soma pecas de domino
lista = [[1,0],[2,3],[6,6]]
def soma_pecas(lista):
    a = 0
    for listas in lista:
        for elementos in listas:
            a += elementos
    return a
    
print(soma_pecas(lista))