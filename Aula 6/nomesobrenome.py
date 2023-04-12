# nome e sobrenome
lista1 = ['ricardo', 'valentina']
lista2 = ['queiroz', 'vergueiro']
def junta_nome_sobrenome(lista1, lista2):
    lista = []
    x = 0
    while x < len(lista1) or x < len(lista2):
        lista.append(lista1[x]+' '+lista2[x])
        x += 1
    return lista

print(junta_nome_sobrenome(lista1, lista2))