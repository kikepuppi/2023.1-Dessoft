# apurando votos
nomes = ['Joaquim', 'Maria', 'Paulo', 'Marta', 'Marcos', 'Lucas']
votos = ['Marta', 'Joaquim', 'Gertrude', 'Carlos', 'Lucas', 'Carlos', 'Joana', 'Gertrude', 'Marcos', 'Carlos', 'Maria', 'Marcos', 'Marta', 'Lucas', 'Marcos', 'Joaquim', 'Gertrude', 'Carlos', 'Gertrude', 'Joana', 'Joana', 'Maria', 'Maria', 'Marcos', 'Paulo', 'Joana', 'Joana', 'Carlos', 'Joana', 'Maria', 'Gertrude', 'Gertrude', 'Marcos', 'Lucas', 'Marcos', 'Marcos', 'Joana', 'Gertrude', 'Marta', 'Gertrude', 'Gertrude', 'Joana', 'Gertrude', 'Paulo', 'Marta', 'Joaquim', 'Paulo', 'Maria', 'Paulo', 'Joana', 'Joana', 'Gertrude', 'Lucas', 'Marcos', 'Paulo', 'Maria', 'Marta', 'Lucas', 'Marcos', 'Paulo', 'Carlos', 'Joana', 'Gertrude', 'Marcos', 'Gertrude', 'Marta', 'Joaquim', 'Marcos', 'Marcos', 'Joaquim', 'Carlos', 'Marcos', 'Marcos', 'Carlos', 'Joana', 'Marta', 'Lucas', 'Marcos', 'Paulo']
def apurando_votos(nomes, votos):
    nomes_jafoi = []
    x = 0
    a_max = 0
    soma_votos = 0
    while x < len(votos):
        if votos[x] not in nomes_jafoi:
            nomes_jafoi.append(votos[x])
            a = list.count(votos,votos[x])
            if votos[x] not in nomes:
                soma_votos += a
            if a >= a_max:
                a_max = a
                y = x
            print(a)
            print(votos[x])
        x += 1
    if votos[y] not in nomes or soma_votos >= a_max:
        return 'CANCELADA'
    return votos[y]
print(apurando_votos(nomes,votos))


    