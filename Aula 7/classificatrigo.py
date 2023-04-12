# classifica o lote de trigo
lista = [2.0, 6.8, 9.0]
def classifica_trigo(lista):
    saida = []
    for i in range(len(lista)):
        a = lista[i]
        if a <= 2:
            saida.append('T1')
        elif a <= 3:
            saida.append('T2')
        elif a <= 7:
            saida.append('T3')
        else:
            saida.append('FT')            
    return(saida)

print(classifica_trigo(lista))