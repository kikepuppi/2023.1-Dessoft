# atmosfera 

def eh_respiravel(lista):
    elementos = []
    for listas in lista:
        for elemento in listas:
            elementos.append(elemento)
    o = elementos.count('O')
    porcentagem = o/len(elementos)
    if porcentagem >= 0.2:
        return True
    else:
        return False

    