# lista crescente ou decrescente
lista = [4,3]
def classifica_lista(lista):
    x = 1
    if len(lista) < 2:
        return 'nenhum'
    elif lista[x] > lista[x-1]:
        while lista[x] > lista[x-1]:
                if x == len(lista) - 1:
                    return 'crescente'
                    break
                x+=1
    elif lista[x] < lista[x-1]:
        while lista[x] < lista[x-1]:
            if x == len(lista) - 1:
                return 'decrescente'
                break
            x+=1
    if x != len(lista)-1:
        return 'nenhum'

print(classifica_lista(lista))