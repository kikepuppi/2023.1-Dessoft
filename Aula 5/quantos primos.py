# quantos primos
def primos_entre(a,b):
    n = a-1
    quantos = 0
    while n < b:
            n += 1
            i = 3
            while True:
                if n == 1:
                    break
                elif n == 2 or n == 3 or n == 5:
                    quantos += 1
                    break
                elif n % 2 == 0:
                    break
                elif n % i == 0:
                    if n != i:
                        break
                    elif n == i:
                        quantos += 1
                        break
                i += 2
    return quantos
print(primos_entre(10,100))