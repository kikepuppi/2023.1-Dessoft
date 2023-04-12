#tudo em segundos

D = float(input('Quantos dias?'))
H = float(input('Quantas horas?'))
M = float(input('Quantos minutos?'))
S = float(input('Quantos segundos?'))

Dseg = D*86400
Hseg = H*3600
Mseg = M*60

Segundos = (Dseg + Hseg + Mseg + S) 
print(Segundos)