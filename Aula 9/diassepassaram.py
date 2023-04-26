# dias se passaram
data = '02/02/2009'
def dias_do_ano(data):
    dia = int(data[0:2])
    mes = int(data[3:5])
    meses = [31,28,31,30,31,30,31,31,30,31,30,31]
    r = dia-1
    if mes == 1:
        return r
    for i in range(mes-1):
        r += meses[i]
    return r

print(dias_do_ano(data))








