# lista de restaurantes

def busca_restaurantes(lista, categoria, valor):
    i = 0
    resultado = []
    while i < len(lista):
        n = lista[i][0]
        c = lista[i][1]
        a = lista[i][2]
        gm = lista[i][3]
        if categoria == 'culinaria':
            if c == valor:
                resultado.append(n)
        if categoria == 'ambiente':
            if a == valor:
                resultado.append(n)
        if categoria == 'preco':
            if gm <= valor:
                resultado.append(n)
        i += 1
    return resultado


lista = [["Ristorante Italiano", "Italiano", "Elegante", 80],["Cantina Mexicana", "Mexicano", "Descontraído", 50],["Sushi Bar Japonês", "Japonês", "Sofisticado", 120],["Comida Vegana", "Vegano", "Alternativo", 60],["Lanchonete do Zé", "Fast-food", "Popular", 20]]
categoria = 'ambiente'
valor = 'Elegante'
print(busca_restaurantes(lista, categoria, valor))
