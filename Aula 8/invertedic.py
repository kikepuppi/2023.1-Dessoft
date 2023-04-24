# inverte o dicionario

dic = {'Ana': 19, 'Bruno': 18, 'João': 19}
def inverte_dicionario(dic):
    dicr = {}
    for k, v in dic.items():
        if v not in dicr.keys():
            dicr[v] = [k]
        else:
            dicr[v].append(k)
    return dicr

print(inverte_dicionario(dic))

