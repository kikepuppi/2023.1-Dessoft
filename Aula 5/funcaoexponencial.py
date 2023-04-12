# Funcao exponencial (e)
import math
x = 2
n = 2
def calcula_euler(x,n):
    i = 0
    e = 0
    while i < n:
        e += x**i/(math.factorial(i))
        i += 1
    return e
print(calcula_euler(x,n))
