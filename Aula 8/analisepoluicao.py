# analise poluicao
p = {
    'Argentina': {'Buenos Aires': 60, 'Córdoba': 70},
    'Brasil': {'Rio de Janeiro': 75, 'São Paulo': -80},
    'Chile': {'Santiago': -40},
    'México': {'Cidade do México': 90}
}

def total_por_pais(p):
    dic2 = {}
    for k, v in p.items():
        for valores in v.values():
            if k not in dic2.keys():
                dic2[k] = abs(valores)
            else:
                dic2[k] += abs(valores)
    return dic2

print(total_por_pais(p))
