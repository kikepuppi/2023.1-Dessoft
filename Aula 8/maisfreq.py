# palavra mais frequente
palavras = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
def mais_frequente(palavras):
    max = 0
    for palavra in palavras:
        i = palavras.count(palavra)
        if i > max:
            max = i
            r = palavra
    return r

print(mais_frequente(palavras))
