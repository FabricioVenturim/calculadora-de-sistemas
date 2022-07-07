import numpy as np

def resolve_sistema(matriz, variaveis):
    """Função que resolve o sistema de equações

    Args:
        matriz (array): matriz formada a partir das equações
        variaveis (lista): lista com as variáveis presentes nas equações passadas
    """    

    #### Zera lado esquerdo ####
    linha_index = 0
    #passa linha por linha
    while linha_index < len(matriz): 
        #em cada linha, passa coluna por coluna até o 1 da matriz identidade 
        for coluna in range(0, linha_index):
            #Multiplica a linha pivo pelo número da linha que desejamos zerar 
            linha_pivo = matriz[coluna] * matriz[linha_index, coluna] 
            #Substitui a linha da matriz pela nova linha escalonada
            matriz[linha_index] = matriz[linha_index] - linha_pivo
        #Colocando o primeiro valor não zero da linha igual a 1
        if matriz[linha_index, linha_index] != 0:
            matriz[linha_index] = matriz[linha_index]/matriz[linha_index, linha_index] 
        linha_index += 1 
    linha_index -= 1
    
    #### Analisar a quantidade de soluções do sistema
    if matriz[linha_index, linha_index] == 0 and matriz[linha_index, linha_index + 1] == 0:
        print("O sistema de equações possui infinitas soluções")
    elif matriz[linha_index, linha_index] == 0:
        print("O sistema de equações é impossível")
    
    else: #### Zera lado direio ####
        #Agora vamos escalonar de baixo para cima
        # linha_index = len(matriz) - 1
        while linha_index >= 0:
            for coluna in range(len(variaveis) - 1, linha_index, -1):
                #em cada linha, passa coluna por coluna até o 1 da matriz identidade 
                linha_pivo = matriz[coluna] * matriz[linha_index, coluna]
                #Substitui a linha da matriz pela nova linha escalonada
                matriz[linha_index] = matriz[linha_index] - linha_pivo
            linha_index -= 1
            
        matriz_final = np.around(matriz, 2)
        for variavel in variaveis:
            index = variaveis.index(variavel)
            print(f"\nO valor da variável {variavel} é: {matriz_final[index][-1]}")

