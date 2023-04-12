# Multa eba

v = float(input('Qual a velocidade?'))

if v > 80:
    multa = (v-80)*5
    print('Você foi multado em {0:.2f} reais'.format(multa))

else:
    print('Não foi multado')