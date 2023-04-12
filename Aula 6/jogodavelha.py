# Jogo da velha matrizes

lista = [['X', 'O', 'O'], ['.', 'O', 'X'], ['O', '.', 'X']]
def verifica_jogo_da_velha(lista):
    lista1 = lista[0]
    lista2 = lista[1]
    lista3 = lista[2]
    print(lista1, lista2, lista3)
    if lista1[0] == lista2[0] and lista1[0] == lista3[0]:
        return lista1[0]
    if lista1[1] == lista2[1] and lista1[1] == lista3[1]:
        return lista1[1]
    if lista1[2] == lista2[2] and lista1[2] == lista3[2]:
        return lista1[2]
    if lista1[0] == lista1[1] and lista1[0] == lista1[2]:
        return lista1[0]
    if lista2[0] == lista2[1] and lista2[0] == lista2[2]:
        return lista2[0]
    if lista3[0] == lista3[1] and lista3[0] == lista3[2]:
        return lista3[0]
    if lista1[0] == lista2[1] and lista1[0] == lista3[2]:
        return lista1[0]
    if lista1[2] == lista2[1] and lista1[2] == lista3[0]:
        return lista1[2]
    else:
        return 'V'
print(verifica_jogo_da_velha(lista))

