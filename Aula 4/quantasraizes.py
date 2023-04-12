# Raizes de uma funcao de segundo grau
a = -3
b=0
c=27

def quantia_de_raizes(a,b,c):
    D = (b**2)-(4*a*c)
    if D > 0:
        return 2
    if D == 0:
        return 1
    if D < 0:
        return 0



