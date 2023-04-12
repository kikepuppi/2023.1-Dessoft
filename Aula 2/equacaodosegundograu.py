# Equacao de segundo grau

def encontra_uma_raiz(a,b,c):
    x = (-b+(((b**2)-(4*a*c))**(1/2)))/(2*a)
    return x

x = encontra_uma_raiz(2,0,-200)
print(x)