# Distancia de Minkowski

def distancia(x1,y1,x2,y2,p):
    D = ((abs(x1-x2))**p + (abs(y1-y2))**p)**(1/p)
    return D

D = distancia(2,2,1,1,1)
print(D)
