# sequencia de collatz
n = 1000
def comprimento(n):
    c = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        c += 1
    return c
cmax = 0
for n in range(1,1000):
    c = comprimento(n)
    if c > cmax:
        numero = n
        cmax = c
print(numero)        

    