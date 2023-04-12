# aumento do salario

salario = 1500

def calcula_aumento(salario):
    if salario > 1250:
        return salario*0.1
    else:
        return salario*0.15

print(calcula_aumento(salario))
    
