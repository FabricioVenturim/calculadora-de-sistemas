from posixpath import split
from re import X
import numpy

#O programa irá perguntar quantas equações tem
#O programa pedirá para a pessoa escrever as equações

#O programa descobrirá quais são as variáveis
#O programa pegará os números de cada variável

def interface():
    quantidade = verifica_int("Quantas equações têm seu sitema? ")
    equacoes = []
    variaveis = []
    multiplos = []

    for num_equacao in range(1, quantidade + 1):
        equacao = input(f"Digite a {num_equacao}ª equação: ")    
        equacoes.append(equacao)
        encontra_variaveis(equacao, variaveis)

    encontra_multiplos(equacoes,variaveis, multiplos)

    print(variaveis)
    print(multiplos)

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


def encontra_variaveis(equacao, variaveis_list):
    caracteres = list(equacao)
    for caractere in caracteres:
        if caractere.isalpha():
            if not caractere in variaveis_list:
                variaveis_list.append(caractere)
    return variaveis_list

def encontra_multiplos(equacoes, variaveis_list, multiplos_list):
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
    return  multiplos_list

