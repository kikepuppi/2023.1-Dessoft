# eh primo 2.0
n = 1312
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        
print(eh_primo(n))