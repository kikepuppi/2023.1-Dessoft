# SENHA DO COFRE HIHIHIHIHIIHIHIHIH

S = 726

def calcula_segredo(S):
    if S < 100 or S > 999:
        return -1
    else:
        Senha = (S//100)+((S//10)%10)+(S%10)
    return Senha