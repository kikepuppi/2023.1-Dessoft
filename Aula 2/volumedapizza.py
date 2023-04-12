# Volume da PIZZA!

import math
pi = math.pi

def volume_da_pizza(z,a):
    V = (pi*(z**2))*a
    return V

V = volume_da_pizza(2,1/pi)
print(V)
