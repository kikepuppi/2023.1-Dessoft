# Distancia x de um projetil

import math
pi = math.pi
g = 9.8

def calcula_distancia_do_projetil(v,θ,y0):
    d = (v**2)/(2*g)*(1+(math.sqrt(1+((2*g*y0)/((v**2)*(math.sin(θ)**2))))))*math.sin(2*θ)
    return d

d = calcula_distancia_do_projetil(10,pi/3,10)
print(d)