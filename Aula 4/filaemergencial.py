# Fila de emergencia VLA

Cor = input('Classificação? (V/L/A)')
V = int(input('Quantos Vermelhos estão aguardando?'))
L = int(input('Quantos Laranjas estão aguardando?'))
A = int(input('Quantos Amarelos estão aguardando?'))

Vf = V*7
Lf = L*5
Af = A*5

if Cor == 'V':
    print(Vf)
elif Cor == 'L':
    print(Lf+Vf)
else:
    print(Af+Lf+Vf)