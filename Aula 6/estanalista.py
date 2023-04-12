# esta na lista
lista = [['libia', 3678],['egito', 5008],['india', 9919],['japao', 13836]]
def esta_na_lista(x, lista):
    return(x in [lista[i][0] for i in range(len(lista))])

print(esta_na_lista('libia', lista))