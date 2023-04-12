# proximo primo
def proximo_primo(n):
    a = True
    m = 0
    if n == 0:
        return 2
    else:
        while m != n:
            n += 1
            i = 3
            while True:
                if n == 1:
                    a = False
                    break
                elif n == 2 or n == 3 or n == 5:
                    a = True
                    m = n
                    break
                elif n % 2 == 0:
                    a = False
                    break
                elif n % i == 0:
                    if n != i:
                        a = False
                        break
                    elif n == i:
                        a = True
                        m = n
                        break
                i += 2
        return m
print(proximo_primo(89))