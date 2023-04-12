# Jaca WARS!!!!

import math
v = float(input('Qual a velocidade?'))
θ = float(input('Qual o angulo?'))

d = ((v**2)*math.sin(2*(math.radians(θ))))/(9.8)
    
if d >= 98 and d <= 102:
    a = 'Acertou!'
    print(a)

elif d < 98:
    b = 'Muito perto'
    print(b)

else:
    c = 'Muito longe'
    print(c)
    



