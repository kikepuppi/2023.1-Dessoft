# Area de um pentagono regular

import math

def area_pentagono(l):
    A = 5*(((l/2)/math.tan(36*math.pi/180))*l/2)
    return A

A = area_pentagono(4)
print(A)

