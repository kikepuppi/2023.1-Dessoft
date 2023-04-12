# Calcular angulo de refacao!
import math
pi = math.pi

# angulo de refracao

def snell_descartes(n1, n2, θ1):
   resultado = (n1*math.sin((math.radians(θ1))))/n2
   θ2 = math.degrees((math.asin(resultado)))
   return θ2


θ1 = 30
n2 = 2
n1 = 1
result = snell_descartes(n1, n2, θ1)
print(result)





