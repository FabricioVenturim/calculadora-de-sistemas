import numpy as np
import sistema

def interface():
    quantidade_de_equacoes = verifica_int("Quantas equações têm seu sitema? ")
    equacoes = []
    variaveis = []

    for num_equacao in range(1, quantidade_de_equacoes + 1):
        equacao = input(f"Digite a {num_equacao}ª equação: ")    
        equacoes.append(equacao)
        encontra_variaveis(equacao, variaveis)

    #Verificar se a quantidade de variaveis é igual a quantidade de equações
    if len(variaveis) != quantidade_de_equacoes:
        print("Desculpe, só consigo trabalhar, ainda, com quantidades iguais de variáveis e equações")
    else:
        multiplos = encontra_multiplos(equacoes,variaveis)
        matriz = np.array(multiplos, dtype="double")
        sistema.resolve_sistema(matriz, variaveis)

def verifica_int(msg):
    while True:
        try: #Ele tenta transformar a resposta do usuário em inteiro
            inteiro = int(input(msg))
        except: #Se houver erro, a looping continua até digitar um int
            print('ERRO! por favor, digite um inteiro válido!')
        else:
            if inteiro <= 0:
                print('ERRO! por favor, digite um inteiro válido!')
            else:
                break #Se ele tiver sucesso, o programa segue normalmente.
    return inteiro


def encontra_variaveis(equacao, variaveis):
    caracteres = list(equacao)
    for caractere in caracteres:
        if caractere.isalpha():
            if not caractere in variaveis:
                variaveis.append(caractere)

def encontra_multiplos(equacoes, variaveis_list):
    multiplos_list = []
    for equacao in equacoes:
        partes = equacao.split()
        numeros_da_equacao = []
        for variavel in variaveis_list:
            if variavel in equacao:
                for parte in partes:
                    #Multiplos
                    if variavel in parte:
                        numero = parte
                        corte = list(numero)
                        for caracter in corte:
                            if not caracter.isnumeric():
                                numero = numero.replace(caracter, "")
                        if numero == "":
                            numero = 1
                        if partes[partes.index(parte) - 1] == "-" or "-" in parte: # Para caso o - esteja junto ou separado
                            numero = -1 * int(numero)
                        numeros_da_equacao.append(int(numero))
            else:
                numeros_da_equacao.append(0)
        #Constante
        for caracter in equacao:
            if caracter == "=":
                constante = int(equacao[equacao.index(caracter) + 1:])
                numeros_da_equacao.append(constante)

        multiplos_list.append(numeros_da_equacao)
    return multiplos_list