from posixpath import split
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

        #Encontra as variáveis
        encontra_variaveis(equacao, variaveis)
        
        #Encontra os múltiplos
        encontra_multiplos(equacao,variaveis, multiplos)

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

def encontra_multiplos(equacao, variaveis_list, multiplos_list):
    partes = equacao.split()
    multiplo = []
    for parte in partes:
        for variavel in variaveis_list:
            if variavel in parte:
                multiplo.append(parte)
    return multiplos_list.append(multiplo)

