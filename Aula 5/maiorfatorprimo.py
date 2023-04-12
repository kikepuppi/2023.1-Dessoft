# maior fator primo
def maior_fator_primo(n):
    i = 2
    while i <= n / i:
        if n % i == 0:
            n /= i
        else:
            i += 1
    return n