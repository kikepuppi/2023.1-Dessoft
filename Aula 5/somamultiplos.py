# soma multiplos
x = 2
y = 5
def soma_multiplos(x,y):
    maior = max(x,y)*10
    n = 2
    total = 0
    while n <= maior:
        if n % x == 0 or n % y == 0:
            total += n
            n += 1
        else:
            n += 1
    return total

print(soma_multiplos(x,y))