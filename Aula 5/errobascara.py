# erro de bascara
import math
def errototal(x):
    senob = (4*x*(180-x))/(40500-x*(180-x))
    senop = math.sin(math.radians(x))
    erro = abs(senob-senop)  
    return erro

erromax = 0
for x in range(91):
    erro = errototal(x)
    if erro > erromax:
        erromax = erro
        n = x    
print(n)