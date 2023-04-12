# Preço da passagem

distancia = float(input('Qual a distancia?'))

if distancia <= 200:
    preco = 0.5*distancia
    print('{0:.2f}'.format(preco))
else:
    preco = 100 + (distancia-200)*0.45
    print('{0:.2f}'.format(preco))