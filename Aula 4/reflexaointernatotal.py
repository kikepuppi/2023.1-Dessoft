# reflexao interna total
import math

def reflexao_total_interna(n1, n2, θ2):
    seno = (n2*math.sin(math.radians(θ2)))/n1

    if seno > 1:
        return True
    else:
        return False
print(reflexao_total_interna(1,1,30))
