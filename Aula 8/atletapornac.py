# atleta por nacionalidade
dic = {
    "Mathieu BILODEAU": {
        "idade": 37,
        "nacionalidade": "Canadá",
        "modalidade": "Atletismo",
    },
    "Gabriela BITOLO": {
        "idade": 22,
        "nacionalidade": "Brasil",
        "modalidade": "Handebol",
    },
    "Jerome BLAKE": {
        "idade": 25,
        "nacionalidade": "Canadá",
        "modalidade": "Atletismo",
    },
    "Felipe BORGES": {
        "idade": 36,
        "nacionalidade": "Brasil",
        "modalidade": "Handebol",
    },
    "Gabriela BRAGA GUIMARAES": {
        "idade": 27,
        "nacionalidade": "Brasil",
        "modalidade": "Vôlei",
    },
}

def agrupa_por_nacionalidade(dic):
    dicr = {}
    for k, v in dic.items():
        if v['nacionalidade'] not in dicr:
            dicr[(v['nacionalidade'])] = [k]
        else:
            dicr[(v['nacionalidade'])].append(k)
    return dicr

print(agrupa_por_nacionalidade(dic))