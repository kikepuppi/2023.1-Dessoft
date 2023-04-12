# reclamacoes e justica

reclamacoesmax = 1
justicamax = 1
reclamacoes = 0.2
justica = 0.9

def meta_atingida(reclamacoesmax, justicamax, reclamacoes, justica):
    if reclamacoes < reclamacoesmax and justica < justicamax:
        return True
    else:
        return False

meta = meta_atingida(reclamacoesmax, justicamax, reclamacoes, justica)
print(meta)