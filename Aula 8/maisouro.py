# mais medalhas de ouro
m = [{
    'nome': ' Michael Phelps',
    'nacionalidade': 'Norte Americano',
    'ouro': 23, 'prata': 3, 'bronze': 2,
},
{
    'nome': 'Larisa Latynina',
    'nacionalidade': 'Russo',
    'ouro': 9, 'prata': 5, 'bronze': 4,
},
{
    'nome': 'Nikolai Andrianov',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 5, 'bronze': 3,
},
{
    'nome': 'Boris Shakhlin',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 4, 'bronze': 2,
},
{
    'nome': 'Jenny Thompson',
    'nacionalidade': 'Norte Americano',
    'ouro': 8, 'prata': 3, 'bronze': 1,
}]

def mais_medalhas(m):
    dic2 = {}
    for i in range(len(m)):
        if m[i]['nacionalidade'] not in dic2:
            dic2[(m[i]['nacionalidade'])] = m[i]['ouro']
        else:
            dic2[(m[i]['nacionalidade'])] += m[i]['ouro']
        max = 0
        for k, v in dic2.items():
            if v > max:
                max = v
                r = k
    return r

print(mais_medalhas(m))
