# PA ou PG
lista = [1,1]
def verifica_progressão(lista):
    x = 1
    if lista[0] == 0:
        if min(lista) == 0 and max(lista) == 0:
            return 'PG'
        rPA = lista[1]-lista[0]
        if (lista[x] == lista[x-1] + rPA):
            while (lista[x] == lista[x-1] + rPA):
                if x == len(lista) - 1:
                    return 'PA'
                    break
                x+=1
        if x != len(lista):
            return 'NA'  
    rPG = lista[1]/lista[0]    
    rPA = lista[1]-lista[0]
    if (lista[x] == lista[x-1] + rPA) and (lista[x] == lista[x-1]*rPG):
        while (lista[x] == lista[x-1] + rPA) and (lista[x] == lista[x-1]*rPG):
            if x == len(lista) - 1:
                return 'AG'
                break
            x+=1
    if (lista[x] == lista[x-1] + rPA):
        while (lista[x] == lista[x-1] + rPA):
            if x == len(lista) - 1:
                return 'PA'
                break
            x+=1
    if (lista[x] == lista[x-1]*rPG):
        while (lista[x] == lista[x-1]*rPG):
            if x == len(lista) - 1:
                return 'PG'
                break
            x+=1
    if x != len(lista):
        return 'NA'
    
print(verifica_progressão(lista))