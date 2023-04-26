# Formata data
data = '2021.11.01'
f = 'a.m.d'
def formata_data(data,f):
    c = f[1]
    fl = []
    for i in range(0,len(f),2):
        fl.append(f[i])
    while len(fl) != 1:
        if fl[0] == 'd':
            a = data.find(c)
            dia = data[0:a]
            data = data[a+1:]
            fl.remove('d')
        elif fl[0] == 'm':
            a = data.find(c)
            mes = data[0:a]
            data = data[a+1:]
            fl.remove('m')
        elif fl[0] == 'a':
            a = data.find(c)
            ano = data[0:a]
            data = data[a+1:]
            fl.remove('a')
    if fl == ['d']:
        dia = data
    if fl == ['m']:
        mes = data
    if fl == ['a']:
        ano = data
    if len(dia) == 1:
        dia = '0'+dia
    if len(mes) == 1:
        mes = '0'+mes
    if len(ano) == 2:
        ano = '20'+ano
    return ano+'-'+mes+'-'+dia

print(formata_data(data,f))