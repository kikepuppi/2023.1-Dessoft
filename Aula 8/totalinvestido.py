# total investido

def soma_investimento(dic):
    dicr = {}
    valores = {}
    for c in dic:
        valores[c] = dic[c]['valor de mercado']
    for c in dic:
        for nome, v in dic[c]['associados'].items():
            if nome in dic.keys():
                dic[nome]['valor de mercado'] += (v/100)*valores[c]
    for c in dic:
        for nome, v in dic[c]['associados'].items():
            if nome not in dicr.keys() and nome not in dic.keys():
                    dicr[nome] = (v/100)*dic[c]['valor de mercado']
            elif nome in dicr.keys() and nome not in dic.keys():
                    dicr[nome] += (v/100)*dic[c]['valor de mercado']
    return dicr

dic = {
    'acme corporation inc': {
        'valor de mercado': 4560000.00,
        'associados': {
            'joao silva matoso': 30,   # 30% da empresa
            'maria santana alves': 70  # 70% da empresa
        }
    },
    'insper solid investiment': {
        'valor de mercado': 8950000.00,
        'associados': {
            'maciel fina pessoa': 10,  # 10% da empresa
            'insper junior ltda': 80,  # 80% da empresa
            'marcio massado': 5,       # 5% da empresa
            'jair designa broncado': 5 # 5% da empresa
        }
    },
    'insper junior ltda':  {
        'valor de mercado': 40200100.00,
        'associados': {
            'maciel fina pessoa': 20, # 20% da empresa
            'joao silva matoso': 30,  # 30% da empresa
            'dario finado': 40,       # 40% da empresa
            'acme corporation inc': 10 # 10% da empresa
        }
    }
}
print(soma_investimento(dic))
