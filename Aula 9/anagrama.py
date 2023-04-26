# Anagrama
p1 = 'cacos'
p2 = 'sacos'
def anagrama(p1,p2):
    p1l = []
    p2l = []
    for i in range(len(p1)):
        p1l.append(p1[i])
    for i in range(len(p2)):
        p2l.append(p2[i])
    p1l = sorted(p1l)
    p2l = sorted(p2l)
    if p1l == p2l:
        return True
    else:
        return False
print(anagrama(p1,p2))

            

