# Distribuição Exponencial

import math

λ = float(input("Qual a taxa (λ)? "))
x = float(input("Qual x, para calcular F(λ, x)? "))

F = 1-(math.e**((-λ)*x))
print('{0:.4f}'.format(F))