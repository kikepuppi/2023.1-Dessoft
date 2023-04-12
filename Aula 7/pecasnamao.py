# possiveis pecas na mao
m = [[0,2],[2,1],[1,6],[6,5],[5,0]]
p = [[1,3],[1,4],[4,6],[2,3],[2,4],[6,6],[2,6]]
def posicoes_possiveis(m,p):
    resultado = []
    if len(m) != 0:
        em = [m[0][0],m[-1][1]]
    for i in range (len(p)):
        if m == []:
            resultado.append(i)
        elif p[i][0] in em or p[i][1] in em:
            resultado.append(i)
    return resultado

print(posicoes_possiveis(m,p))



    

