# Calcular volume de uma esfera de raio x

import math
pi = math.pi

def calcula_volume_da_esfera(raio):
    volume = 4/3*(pi*(raio**3))
    return volume

raio = 3
volume = calcula_volume_da_esfera(raio)
print(volume)