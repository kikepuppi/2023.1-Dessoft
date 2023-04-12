# estima pi v2

n = 3
def PiWallis(n):
    i = 0
    cima = 2
    baixo = 1
    soma = 1
    while i < n:
        i += 1
        soma = soma*(cima/baixo)
        if i < n:
            baixo += 2
            soma = soma*(cima/baixo)
            cima += 2
            i += 1
    pi = soma*2
    return pi

print(PiWallis(n))

    