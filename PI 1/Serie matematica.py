# Serie matematica PI
import math
def calcula_serie(n):
    i = 0
    a = 1
    soma = 0
    while i < n:
        soma += ((2**i)*(math.factorial(a)))/(5*(3**a))
        i += 1
        a += 1
    return soma