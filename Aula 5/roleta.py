# roleta simplificada
import random
d = 100
while True:
    if d <= 0:
        break
    print(d)
    a = float(input('aposta'))
    if a == 0:
        break
    np = input('numero ou paridade? [n/p]')
    if np == 'n':
        nu = int(input('numero de 1 a 36?'))
    if np == 'p':
        pu = input('par ou impar? [p,i]')
    numero = random.randint(0,36)
    if np == 'p' and pu == 'p' and numero % 2 == 0:
        d += a
    elif np == 'p' and pu == 'i' and numero % 2 != 0:
        d += a
    elif np == 'p':
        d -= a
    elif np == 'n' and numero == nu:
        d += a*35
    elif np == 'n':
        d -= a
