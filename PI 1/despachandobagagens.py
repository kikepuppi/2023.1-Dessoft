# despachando bagagens
f = [ [1, 10], [0, 23], [2, 32] ]
d = [ [1, 22], [2, 31, 32] ]
def chave(listas):
    return listas[0]
def valores_a_pagar(f,d):
    resultado = []
    for listas in d:
        d.sort(key=chave)
    for i in range (len(f)):
        total = 0
        if d[i][0] != i:
            d.insert(i,[0,0])
        if len(d[i]) - 1 > f[i][0]:
            total += ((len(d[i]) - 1) - (f[i][0]))*300
        for a in range (1,len(d[i])):
            if d[i][a] > f[i][1]:
                total += (d[i][a] - f[i][1])*50
        resultado.append(total)
    return resultado

print(valores_a_pagar(f,d))