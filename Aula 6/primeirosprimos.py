# lista de n primeiros primos

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def lista_primos(n):
    lista = []
    i = 0
    while len(lista) < n:
        if eh_primo(i) == True:
            lista.append(i)
        i += 1
    return lista

print(lista_primos(3))