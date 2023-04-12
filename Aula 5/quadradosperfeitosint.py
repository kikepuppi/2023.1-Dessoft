# quadrados perfeitos no intervalo
import math
a = 0
b = 5

def quadrados_no_intervalo(a,b):
    quantos = 0
    i = a
    while i >= a and i <= b:
        if i == (int(math.sqrt(i)))**2:
            quantos += 1
        i += 1
    return quantos

print(quadrados_no_intervalo(a,b))
            

