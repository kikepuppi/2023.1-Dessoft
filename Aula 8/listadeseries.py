# Lista de series
l =  [
    {"plataforma": "Netflix", "titulo": "Between", "ano_estreia": 2015},
    {"plataforma": "Prime Video", "titulo": "Humans", "ano_estreia": 2015},
    {"plataforma": "Disney+", "titulo": "LEGO Star Wars", "ano_estreia": 2016},
    {"plataforma": "Disney+", "titulo": "Marvel's Inhumans", "ano_estreia": 2017},
    {"plataforma": "Disney+", "titulo": "Best Friends Whenever", "ano_estreia": 2015},
]
ano = 2015
def mais_lancamentos(l,ano):
    dic = {}
    for i in range (len(l)):
        if l[i]["ano_estreia"] == ano:
            if l[i]["plataforma"] not in dic.keys():
                dic[(l[i]["plataforma"])] = 1
            else:
                dic[(l[i]["plataforma"])] += 1
    max = 0
    r = []
    for k, v in dic.items():
        if v >= max:
            max = v
    for k, v in dic.items():
        if v == max:
            r.append(k)
    return r

print(mais_lancamentos(l,ano))

