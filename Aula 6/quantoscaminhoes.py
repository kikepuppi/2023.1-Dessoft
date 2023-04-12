# quantos caminhoes

def quantos_caminhoes(lista):
    sum = 0
    i = 1
    for c in range (len(lista)):
        if sum + lista[c] <= 2000:
            sum += lista[c]
        elif sum + lista[c] > 2000:
            sum = lista[c]
            i += 1
    return i

print(quantos_caminhoes([1000, 500, 400, 200, 50, 450, 1300, 500, 1450, 100]))