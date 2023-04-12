# calculadora simplificada QUIZ 2

i = float(input())
while True:
    operador = input('')
    while operador != '+' and operador != '-' and operador != '/' and operador != '*' and operador != '=':
        print("Deveria ser um dos seguintes operadores: + - / * ou o =")
        operador = input('')
    if operador == '=':
        print(i)
        break
    numero = float(input())
    if operador == '+':
        i += numero
    elif operador == '-':
        i -= numero
    elif operador == '/':
        i /= numero
    elif operador == '*':
        i *= numero


