# calcula estado
lista = [['Maria', [5.0, 10.0, 0.0, 10.0, 10.0], [6.7, 8.0]], ['Joao', [0.0, 10.0, 10.0, 10.0, 0.0], [6.7, 2.0]], ['Joana', [10.0, 0.0, 10.0, 0.0, 10.0], [6.7, 8.0]]]
def calcula_estado(lista):
    listatotal = []
    for i in range(len(lista)):
        nome = lista[i][0]
        quizzes = lista[i][1]
        AI = lista[i][2][0]
        AF = lista[i][2][1]
        mediaq = (sum(quizzes)-min(quizzes))/len(quizzes)-1
        media = 0.1*mediaq + 0.4*AI + 0.5*AF
        resultado = []
        resultado.append(nome)
        if media >= 5:
            resultado.append('A')
        else:
            resultado.append('R')
        listatotal.append(resultado)
    return listatotal

print(calcula_estado(lista))