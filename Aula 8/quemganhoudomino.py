# quem ganhou domino
dic = {
    0: [],
    1: [[1,1],[1,2],[0,0],[1,4],[1,5]],
    2: [[3,6],[2,4],[3,4],[2,3]],
    3: [[3,5],[4,4],[4,5],[0,2],[5,5],[5,6],[0,5]]
}
def verifica_ganhador(dic):
    y = -1
    for i in dic.keys():
        if len(dic[i]) == 0:
            y = i
    return y

print(verifica_ganhador(dic))