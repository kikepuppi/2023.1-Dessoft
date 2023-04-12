# MRU
def calcula_posicao(t,s0,v):
    posicao = s0 + (v*t)
    return posicao

t = 2
v = 10
s0 = 0
posicao = calcula_posicao(t,s0,v)
print(posicao)