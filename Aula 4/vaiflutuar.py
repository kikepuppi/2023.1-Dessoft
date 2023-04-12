# vai boiar?

import math
pi = math.pi

def will_it_float(P, R, r):
    densidade = P*1000/(2*(pi**2)*R*(r**2)) # Tudo em g/cm3
    if densidade <= 0.997:
        return True
    else:
        return False

print(will_it_float(1,10,10))


