# apura votos por area
vs = [{'secao': 102,'area': 'litoral','candidatos': {'ze da esquina': 159,'maria do milagre': 231,'nulos': 43,'brancos': 43}},{'secao': 103,'area': 'litoral','candidatos': {'ze da esquina': 432,'maria do milagre': 965,'nulos': 63,'brancos': 86}},{'secao': 431,'area': 'capital','candidatos': {'tiao da borracharia': 723,'maria do milagre': 812,'nulos': 3,'brancos': 36}}]
cp = {'fdb': ['tiao da borracharia', 'frederico ganhador', 'zelia despachante'],'ipdt': ['ze da esquina', 'maria do milagre']}
def apura_area(vs, cp):
    dicresult = {}
    for dic in vs:
        if dic['area'] not in dicresult.keys():
            dicresult[dic['area']] = {}
        for k, v in dic['candidatos'].items():
            for partido, candidatos in cp.items():
                if k in candidatos:
                    if partido not in dicresult[dic['area']]:
                        dicresult[dic['area']][partido] = v
                    else:
                        dicresult[dic['area']][partido] += v             
            if k == 'nulos':
                if 'nulos' not in dicresult[dic['area']].keys():
                    dicresult[dic['area']]['nulos'] = v
                else:
                    dicresult[dic['area']]['nulos'] += v
            if k == 'brancos':
                if 'brancos' not in dicresult[dic['area']].keys():
                    dicresult[dic['area']]['brancos'] = v
                else:
                    dicresult[dic['area']]['brancos'] += v
    return dicresult

        


print(apura_area(vs,cp))