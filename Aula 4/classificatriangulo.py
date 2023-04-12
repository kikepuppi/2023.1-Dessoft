# Classificador de triangulo

def classifica_triangulo(lado1, lado2, lado3):
    if lado1==lado2 and lado1==lado3:
        return 'equilátero'
    elif lado1==lado2 and lado1!=lado3:
        return 'isósceles'
    elif lado1!=lado2 and lado1==lado3:
        return 'isósceles'
    elif lado2==lado3 and lado2!=lado1:
        return 'isósceles'
    else:
        return 'escaleno'
print(classifica_triangulo(1,1,2))
print(classifica_triangulo(1,2,2))
print(classifica_triangulo(1,2,3))