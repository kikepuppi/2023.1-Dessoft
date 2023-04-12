# matriz valor absoluto

lista = [[1, 2, -3], [4, 5, 6], [7, 8, -9]]

def maior_absoluto(lista):
    valores = []
    for listas in lista:
        for numero in listas:
            valores.append(abs(numero))
    return max(valores)

print(maior_absoluto(lista))



