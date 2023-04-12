# Nivel IDH

IDH = 0.7

def nivel_idh(IDH):
    if IDH >= 0.8 and IDH <= 1:
        return 'Muito Alto'
    elif IDH >= 0.7 and IDH < 0.8:
        return 'Alto'
    elif IDH >= 0.555 and IDH < 0.7:
        return 'Médio'
    elif IDH >= 0.35 and IDH < 0.555:
        return 'Baixo'
    elif IDH < 0.35:
        return 'Sem dados'

IDH = nivel_idh(IDH)
print(IDH)

    