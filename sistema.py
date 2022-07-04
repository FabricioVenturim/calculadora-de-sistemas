import numpy as np

def resolve_sistema(matrix, variaveis):
    zera_colunas(matrix, variaveis)
    for variavel in variaveis:
        index = variaveis.index(variavel)
        print(f"O valor da variável {variavel} é: {matrix[index][-1]}")

def zera_colunas(matrix, variaveis):
    #Zera lado esquerdo
    linha_index = 0
    while linha_index < len(matrix): #passa linha por linha
        for coluna in range(0, linha_index): #em cada linha, passa coluna por coluna
            linha_pivo = matrix[coluna] * matrix[linha_index, coluna] #Multiplica a linha pivo pelo número  da linha que desejamos zerar
            matrix[linha_index] = matrix[linha_index] - linha_pivo
        matrix[linha_index] = matrix[linha_index]/matrix[linha_index, linha_index] # Coloca os valores 1
        linha_index += 1

    #Zera lado direio
    linha_index = len(matrix) - 1
    while linha_index >= 0:
        for coluna in range(len(variaveis) - 1, linha_index, -1):
            linha_pivo = matrix[coluna] * matrix[linha_index, coluna]
            matrix[linha_index] = matrix[linha_index] - linha_pivo
        linha_index -= 1
