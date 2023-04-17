# media de idade dos atletas

def calcula_media(dic,pais):
    atletas = []
    for atleta in dic:
        if pais in dic[atleta].values():
            atletas.append(dic[atleta]['idade'])
    return sum(atletas)/len(atletas)

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
        "idade": 26,
        "nacionalidade": "Brasil",
        "modalidade": "Vôlei",
    },
}

pais = 'Brasil'

print(calcula_media(dic,pais))