# 100 metros rasos

def calcula_tempo(dic):
    dic2 = {}
    for i in dic.keys():
        dic2[i] = (200/dic[i])**0.5
    return dic2