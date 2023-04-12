# classificador de idade

idade = 10

def classifica_idade(idade):
    if idade <= 11:
        return 'crianca'
    elif idade >= 12 and idade <= 17:
        return 'adolescente'
    else:
        return 'adulto'

resultado = classifica_idade(idade)
print(resultado)

    

