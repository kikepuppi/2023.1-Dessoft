# Distancia euclidiana

def distancia_euclidiana(x1,x2,y1,y2):
    distancia = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return distancia

x1 = 2
y1 = 2
x2 = 1
y2 = 2
distancia = distancia_euclidiana(x1,x2,y1,y2)
print(distancia)