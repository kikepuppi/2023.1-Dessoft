# fibonacci
n = 4
def calcula_fibonacci(n):
    x = 0
    lista = []
    while x < n:
        if x == 0 or x == 1:
            lista += [1]
        else:
            lista += [lista[x-1] + lista[x-2]]
        x += 1
    return lista

print(calcula_fibonacci(n))



