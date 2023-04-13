# Conta ocorrencia de palavras
lista = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']
def conta_ocorrencias(lista):
    ocorrencias = {}
    for palavra in lista:
        if palavra in ocorrencias:
            ocorrencias[palavra] += 1
        else:
            ocorrencias[palavra] = 1
    return ocorrencias

print(conta_ocorrencias(lista))

