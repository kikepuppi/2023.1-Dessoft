# gerando direcoes 

def gera_direcoes(x, y):
    direcoes = ['norte', 'sul', 'leste', 'oeste', 'nordeste', 'noroeste', 'sudeste','sudoeste']
    coordenadas = []
    resultado = []
    for i in range (len(x)):
        coordenadas.append([x[i], y[i]])
        if i != 0:
            if coordenadas[i-1][0] != coordenadas[i][0] and coordenadas[i-1][1] != coordenadas[i][1]:
                if coordenadas[i][0] == coordenadas[i-1][0] + 1 and coordenadas[i][1] == coordenadas[i-1][1] + 1:
                    resultado.append(direcoes[6])
                if coordenadas[i][0] == coordenadas[i-1][0] + 1 and coordenadas[i][1] == coordenadas[i-1][1] - 1:
                    resultado.append(direcoes[4])
                if coordenadas[i][0] == coordenadas[i-1][0] - 1 and coordenadas[i][1] == coordenadas[i-1][1] + 1:
                    resultado.append(direcoes[7])
                if coordenadas[i][0] == coordenadas[i-1][0] - 1 and coordenadas[i][1] == coordenadas[i-1][1] - 1:
                    resultado.append(direcoes[5])
            elif coordenadas[i-1][0] != coordenadas[i][0] and coordenadas[i-1][1] == coordenadas[i][1]:
                if coordenadas[i][0] == coordenadas[i-1][0] + 1:
                    resultado.append(direcoes[2])
                if coordenadas[i][0] == coordenadas[i-1][0] - 1:
                    resultado.append(direcoes[3])
            elif coordenadas[i-1][0] == coordenadas[i][0] and coordenadas[i-1][1] != coordenadas[i][1]:
                if coordenadas[i][1] == coordenadas[i-1][1] + 1:
                    resultado.append(direcoes[1])
                if coordenadas[i][1] == coordenadas[i-1][1] - 1:
                    resultado.append(direcoes[0])
    return resultado

x = [0, 1, 2, 2, 1, 0]
y = [0, 0, 1, 2, 3, 3]
print(gera_direcoes(x, y))
        

            

