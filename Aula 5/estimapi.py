# Estima Pi

a = 1
n = 6
soma = 0
def calcula_pi(a,n,soma):
    while True:
        if a <= n:
            b = 6/(a)**2
            a = a+1
            soma += b
        else:
            break
    result = soma**(1/2)
    return (result)

print(calcula_pi(a,n,soma))
