# norma de um vetor
lista = [3,4,5]
def calcula_norma(lista):
    soma = 0
    for x in range (len(lista)):
        soma += (lista[x])**2
    total = abs(soma**(1/2))
    return total
print(calcula_norma(lista))