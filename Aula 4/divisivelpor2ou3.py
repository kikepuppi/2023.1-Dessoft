# Divisivel por 2 ou 3

numero = 7

def divisivel(numero):
    if numero % 2 == 0 and numero % 3 == 0:
        a = 'Insper'
        return a
    elif numero % 2 == 0:
        b = 'Ins'
        return b
    elif numero % 3 == 0:
        c = 'per'
        return c
    else:
        d = numero
        return d
resultado = divisivel(numero)
print(resultado)

    