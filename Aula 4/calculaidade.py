# Calcula a idade

dia1 = 1
mes1 = 1
ano1 = 2000
dia2 = 2
mes2 = 1
ano2 = 2021

def calcula_idade(dia1, mes1, ano1, dia2, mes2, ano2):
    if mes2 > mes1:
        return (ano2-ano1)
    elif mes2 == mes1 and dia2 >= dia1:
        return (ano2-ano1)
    else:
        return (ano2-ano1)-1

idade = calcula_idade(dia1,mes1,ano1,dia2,mes2,ano2)
print(idade)