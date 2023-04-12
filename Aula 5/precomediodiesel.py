# preco médio diesel

d = int(input('Quantos dias?'))
dt = 0
soma = 0

while True:
    if dt >= d:
        break
    else:
        precod = float(input('Quanto nesse dia?'))
        dt += 1
        soma += precod

total = soma/d
print('O preço médio cobrado foi de {0:.2f}'.format(total))