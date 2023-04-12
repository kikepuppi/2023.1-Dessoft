# decimal para binario
n = 670234
def decimal_para_binario(n):
    a = ''
    if n < 0:
        return 'Negativo'
    else:
        while n > 0:
            if n % 2 == 0:
                a += '0'
            if n % 2 == 1:
                a += '1'
            n = n//2
        return a[::-1]

print(decimal_para_binario(n))