# Medida de um cateto de um triangulo retangulo

def encontra_cateto(h,c1):
    c2 = (h**2 - c1**2)**(1/2)
    return c2

c2 = encontra_cateto(5,4)
print(c2)