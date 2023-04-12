# IRRF

salario = float(input('Qual o salario?'))
dependentes = float(input('Qual o numero de dependentes?'))

def base_de_calculo(salario, dependentes):
    if salario <= 1045:
        return (salario - (0.075*salario) - (dependentes*189.59))
    elif salario >= 1045.01 and salario <= 2089.60:
        return (salario - (0.09*salario) - (dependentes*189.59))
    elif salario >= 2089.61 and salario <= 3134.40:
        return (salario - (0.12*salario) - (dependentes*189.59))
    elif salario >= 3134.41 and salario <= 6101.06:
        return (salario - (0.14*salario) - (dependentes*189.59))
    else:
        return (salario - 671.12 - (dependentes*189.59))

base = base_de_calculo(salario, dependentes)

def calcula_irrf(base):
    if base <= 1903.98:
        return base*0 - 0
    elif base >= 1903.99 and base <= 2826.65:
        return base*0.075 - 142.8
    elif base >= 2826.66 and base <= 3751.05:
        return base*0.15 - 354.8
    elif base >= 3751.06 and base <= 4664.68:
        return base*0.225 - 636.13
    else:
        return base*0.275 - 869.36

irrf = calcula_irrf(base)
print(irrf)

    

