# quantos uns
n = 1010101010
def quantos_uns(n):
    uns = 0
    while n >= 1:
        if n % 10 == 1:
            uns += 1
        n = n//10
    return uns
print(quantos_uns(n))


        


