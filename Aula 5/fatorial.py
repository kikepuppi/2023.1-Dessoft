# fatorial
n = 4
def fatorial(n):
    x = 1
    f = 1
    while x <= n:
        f = f*x
        x += 1
    return f
print(fatorial(n))