# MDC
x = 390
y = 800
def maximo_divisor_comum(x,y):
    i = 3
    n = 1
    while x % 2 == 0 and y % 2 == 0:
        x = x/2
        y = y/2
        n = n*2
    while i <= x and i <= y:
        if x % i == 0 and y % i == 0:
            while x % i == 0 and y % i == 0:
                x = x/i
                y = y/i
                n = n*i
        if x % i != 0 or y % i != 0:
            i += 2
    return n
print(maximo_divisor_comum(x,y))
