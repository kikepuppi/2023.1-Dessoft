# Equacao Gaussiana

import math
pi = math.pi

def calcula_gaussiana(x,μ,σ):
    f = (1/(σ*(math.sqrt(2*pi))))*(math.e**(-0.5*(((x-μ)/σ)**2)))
    return f

f = calcula_gaussiana(0,0,1)
print(f)