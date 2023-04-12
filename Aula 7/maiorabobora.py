# haloween ABROBRA MAIOR
e = 'moranga'
f = [[],[[6.2, 'kabotia'], [5.5, 'moranga']],[[4.2, 'moranga']]]
def maior_abobora(e,f):
    if len(f) == 1 and len(f[0]) == 0:
        return -1
    max = 0
    indice = -1
    for i in range(len(f)):
        if len(f[i]) != 0:
            for j in range(len(f[i])):
                if f[i][j][1] == e:
                    if f[i][j][0] > max:
                        max = f[i][j][0]
                        indice = i
    
    return indice

print(maior_abobora(e,f))