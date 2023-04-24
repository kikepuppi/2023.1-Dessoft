# estado mais populcoso
brasil = {
    "São Paulo": {"São Paulo": 21571281, "Campinas": 3224443},
    "Minas Gerais": {"Belo Horizonte": 2385639, "Uberlândia": 611903},
}
def mais_populoso(brasil):
    max = 0
    for k, v in brasil.items():
        pop = 0
        for valores in v.values():
            pop += valores
        if pop > max:
            max = pop
            r = k
    return r

print(mais_populoso(brasil))