# PEDRA PAPEL TESOURAAAAAAA

a = "Escolha pedra, papel ou tesoura para jogar"
b = 'empate'
c = 'um'
d = 'dois'

def pedra_papel_tesoura(jogador1, jogador2):
    if (jogador1 == 'pedra' and jogador2 == 'pedra') or (jogador1 == 'tesoura' and jogador2 == 'tesoura') or (jogador1 == 'papel' and jogador2 == 'papel'):
        return b
    elif (jogador1 == 'pedra' and jogador2 == 'tesoura') or (jogador1 == 'tesoura' and jogador2 == 'papel') or (jogador1 == 'papel' and jogador2 == 'pedra'):
        return c
    elif (jogador2 == 'pedra' and jogador1 == 'tesoura') or (jogador2 == 'tesoura' and jogador1 == 'papel') or (jogador2 == 'papel' and jogador1 == 'pedra'):
        return d
    else:
        return a

jogador1 = 'luis'
jogador2 = 'luis'

print(pedra_papel_tesoura(jogador1,jogador2))