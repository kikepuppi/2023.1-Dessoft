# Reducao na vida de um fumante

cf = float(input('quantos cigarros voce fuma por dia?'))
af = float(input('a quantos anos voce fuma?'))

d = af*365
cigarros = d*cf
dias = cigarros*(10/(60*24))

print('voce teve uma reducao de {0} dias'.format(dias))
