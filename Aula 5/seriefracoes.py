# serie fracoes
a = 1
b = 2
n = 3
def calcula_serie(a,b,n):
    contador = 0
    i = 0
    while contador < n:
        i += 1/a**(contador*b)
        contador += 1
    return i

print(calcula_serie(a,b,n))