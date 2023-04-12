# add em ordem
pais = 'zimbabwe'
distancia = 100000
lista = [['libia', 3678],['franca', 3998],['egito', 5008],['india', 9919],['japao', 13836]]
def adiciona_em_ordem(pais, distancia, lista):
    listaentrando = [pais,distancia]
    for listas in lista:
        if pais in listas:
            return lista
    l = len(lista)
    i = 0
    if l == 0:
        lista.append(listaentrando)
        return lista
    if distancia > lista[l-1][1]:
        lista.append(listaentrando)
        return lista
    while lista[i][1] <= distancia:
        i += 1
    lista.insert(i,listaentrando)
    return lista

print(adiciona_em_ordem(pais,distancia,lista))

    
