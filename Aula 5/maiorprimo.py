# maior primo

n = 1234

def eh_primo(n):
    i = 3
    while True:
        if n == 1:
            return False
        elif n == 2 or n == 3 or n == 5:
            return n
        elif n % 2 == 0:
            return False
        elif n % i == 0:
            if n != i:
                return False
            elif n == i:
                return n
        i += 2

def maior_primo_menor_que(n):
    maior_numero = 0
    y = -1
    if eh_primo(n) == True:
        return n
    for n in range(n+1):
        numero = eh_primo(n)
        if numero > maior_numero:
            y = numero
            maior_numero = numero
    return y

print(maior_primo_menor_que(n))        





    