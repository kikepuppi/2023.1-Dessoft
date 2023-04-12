# acougue online

lista = [['patinho','bovina',40],['acem','bovina',34],['peito','frango',24],['sobrecoxa','frango',13],['bisteca','suína',28]]
b = 0
total = 0
carnespedidas = []
c = ''
tudo = []
pesobovino = 0
precobovino = 0
precototal = 0
for listas in lista:
    for elementos in listas:
        tudo.append(elementos)
while c != 'pagar':
    while True:
        c = input('Qual carne?')
        if c == 'pagar':
            break
        for listas in lista:
            carne = listas[0]
            tipo = listas[1]
            valor = listas[2]
            carnespedidas.append(tipo)
            if c not in tudo:
                print("Carne nao reconhecida - tente novamente.")
                break
            if c in tudo:
                if carne == c:
                    p = float(input('Qual o peso?'))
                    peso = p
                    bj = input('Deseja Bandeija? (s/n)')
                    preco = p*valor
                    if peso >= 1 and bj == 's':
                        while p >= 1:
                            p -= 1
                            b += 0.5
                    if tipo == 'bovina':
                        pesobovino += peso
                        precobovino += preco
                    elif tipo != 'bovina':
                        precototal += preco                 
                    break
if pesobovino >= 3:
    if pesobovino >= 5:
        precobovino -= 0.07*precobovino
    else:
        precobovino -= 0.05*precobovino
total = precototal + b + precobovino
if 'bovina' in carnespedidas and 'frango' in carnespedidas and 'suína' in carnespedidas:
    total -= 0.1*total
print("O total da sua compra foi {0:.2f}".format(total))
