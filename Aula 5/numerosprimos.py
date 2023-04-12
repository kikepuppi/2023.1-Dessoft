# Numeros primos

n = 97

def eh_primo(n):
    i = 3
    while True:
        if n == 1:
            return False
        elif n == 2 or n == 3 or n == 5:
            return True
        elif n % 2 == 0:
            return False
        elif n % i == 0:
            if n != i:
                return False
            elif n == i:
                return True
        i += 2

print(eh_primo(n))