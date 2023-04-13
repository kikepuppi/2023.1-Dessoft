# elementos nocivos
lista = [ [ ['O' , 'N' , 'He'],['Ar', 'O', 'He'],['Uuo', 'O', 'O' ] ],
    [ ['H' , 'C' , 'B' ],['O', 'Ar'],['F'  , 'S', 'O', 'He' ] ],
    [ ['Ar', 'Ga', 'Al'],['Ar', 'O', 'Ne'],['O', 'Se'] ]
]
def concentracao_nociva(lista):
    dic = {}
    dicporcentagem = {}
    dicresult = {}
    listatodos = []
    listaunicos = []
    for listas in lista:
        for elemento in listas:
            for elementoss in elemento:
                listatodos.append(elementoss)
    for elementos in listatodos:
        if elementos not in listaunicos:
            listaunicos.append(elementos)
    for i in range (len(listaunicos)):
        dicporcentagem[listaunicos[i]] = (listatodos.count(listaunicos[i])/len(listatodos))*100
    for k, v in dicporcentagem.items():
        if k == 'O' and v < 20:
            dicresult['O'] = v
        if 'O' not in dicporcentagem:
            dicresult['O'] = 0.0
        if k == 'N' and v > 70:
            dicresult['N'] = v
        if k != 'O' and k != 'N' and v > 2:
            dicresult[k] = v
    return dicresult
print(concentracao_nociva(lista))   
    
