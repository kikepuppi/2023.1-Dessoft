# valida calc

# "+", "-", "*", "/", "**", "//", "%"

# ultimo = '='

def valida_entradas(lista):
    l = len(lista)
    if l == 0 or l == 1:
        return False
    i = 1
    while i < len(lista)-1:
        if lista[i] != "+" and lista[i] != "-" and lista[i] !=  "*" and lista[i] !=  "/"and lista[i] !=  "**" and lista[i] !=  "//" and lista[i] !=  "%":
            return False
        i += 2
    if lista[-1] != '=':
        return False
    return True

print(valida_entradas(['1', '+', '1', '1']))