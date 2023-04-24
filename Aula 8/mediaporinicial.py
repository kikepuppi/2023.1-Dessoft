nomes = {
    'Andrew Ayres': 6,
    'Fábio Ikeda': 10,
    'Fábio Kurauchi': 9,
    'Raul Hage': 8
 }

def medias_por_inicial(nomes):
    dic = {}
    qnt = []
    for k, v in nomes.items():
        i = k[0]
        qnt.append(i)
        if i not in dic.keys():
            dic[i] = v
        else:
            dic[i] += v
    for k, v in dic.items():
        c = qnt.count(k)
        dic[k] = v/c
    return dic

print(medias_por_inicial(nomes))


