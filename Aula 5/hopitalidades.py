# hospital idades
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
while True:
    i = int(input('Qual a sua idade?'))
    if i < 0:
        break
    else:
        if i >= 0 and i <= 11:
            a += 1
        if i > 11 and i <=17:
            b += 1
        if i > 17 and i <= 25:
            c += 1
        if i > 25 and i <= 35:
            d += 1
        if i > 35 and i <= 59:
            e += 1
        if i > 59:
            f += 1

media = a+b+c+d+e+f
ap = a*100/media
bp = b*100/media
cp = c*100/media
dp = d*100/media
ep = e*100/media
fp = f*100/media
print('0-11 anos: {0:.2f} %\n12-17 anos: {1:.2f} %\n18-25 anos: {2:.2f} %\n26-35 anos: {3:.2f} %\n36-59 anos: {4:.2f} %\nAcima de 60 anos: {5:.2f} %'.format(ap,bp,cp,dp,ep,fp))