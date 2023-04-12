# Frete

valortotaldopedido = 10000
quantidadedeitensnopedido = 0
frageis = 0
distancia = 0

def calcula_frete(valortotaldopedido, quantidadedeitensnopedido, frageis, distancia):
    if frageis == 'S':
        valorseguro = 0.0175*valortotaldopedido
    if frageis == 'N':
        valorseguro = 0.008*valortotaldopedido
    
    Valorbase = 12.75

    valordofreteporkm = distancia*1.82

    if quantidadedeitensnopedido % 40 > 0:
        quantidadedecaixas = (quantidadedeitensnopedido//40) + 1
    else:
        quantidadedecaixas = quantidadedeitensnopedido//40

    ValorFrete = Valorbase + quantidadedecaixas * valordofreteporkm + valorseguro

    return ValorFrete


