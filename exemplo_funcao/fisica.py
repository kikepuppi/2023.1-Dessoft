def calcula_posicao(posicao_inicial, velocidade_inicial, aceleracao, tempo_decorrido):
    resultado = (posicao_inicial + (velocidade_inicial*tempo_decorrido + (aceleracao*(tempo_decorrido**2)/2)))
    return resultado
