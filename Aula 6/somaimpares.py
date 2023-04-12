# soma impares

lista = [1,2,3,4,5,9]
def soma_impares(lista):
    x = 0
    total = 0
    while x < len(lista):
        if lista[x] % 2 == 1:
            total += lista[x]
        x += 1
    return total

print(soma_impares(lista))