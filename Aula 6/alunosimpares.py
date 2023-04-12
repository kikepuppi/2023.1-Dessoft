# alunos impares
lista = ['henrique', 'gabriel', 'cleiton', 'japita', 'josefina']
def alunos_impares(lista):
    alunos_impares = []
    x = 0
    while x < (len(lista)):
        if x % 2 == 1:
            alunos_impares.append(lista[x])
        x += 1
    return alunos_impares

print(alunos_impares(lista))
