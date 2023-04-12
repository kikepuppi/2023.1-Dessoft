# aproximando pi
import math
def aproxima(n):
    contador = 1
    soma = 0
    i = 3
    while contador < n:
        if contador % 2 == 0:
            soma += 1/(i*(3**contador))
        if contador % 2 != 0:
            soma -= 1/(i*(3**contador))
        contador += 1
        i += 2
    conta = math.sqrt(12)*(1+(soma))
    return conta

print(aproxima(180))

    
