# soma calculadora


a = input('qual o primeiro numero?')
if not a.isdigit():
    print (' digite um numero!')
    exit()
else:
    a = float(a)


b = input('qual o segundo numero?')
if not b.isdigit():
    print (' digite um numero!')
    exit()
else:
    b = float(b)

operador = input('qual operador vc quer?')

if operador == '+':
    print (a + b)
if operador == '-':
    print (a - b)
if operador == '*':
    print (a * b)
if operador == '/':
    print (a / b)
else:
    print('erro')
    