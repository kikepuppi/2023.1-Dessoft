# Prestacao

casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o salario?'))
anos = float(input('Quantos anos pra pagar?'))

if (casa/(anos*12)) > 0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')