#Importe o JSON para iniciar a tarefa:

import json

"""Defina a função que lerá o arquivo:
def readJsonFile(fileName):
Abaixo da definição do arquivo, adicione uma variável de dados como uma string vazia:
data=""         
Para o corpo da função, abra o arquivo json usando a função open e analise o arquivo usando json.load.
def readJsonFile(fileName):
    data = ""
    with open('files/insulin.json') as json_file:
        data = json.load(json_file)
    return data
A função open retorna um manipulador de arquivos para o arquivo files/insulin.json.

json.load lê o arquivo JSON e retorna o conteúdo como um dicionário Python.

Adicione um bloco try/except para tornar a função mais confiável:"""

"""def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data"""

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data

"""aso não seja possível abrir o arquivo, o programa exibirá o 
erro Could not read file (Não foi possível ler o arquivo).
A string data retornada ficará vazia caso o método open file não funcione.
Você criou um módulo jsonFileHandle que pode importar em outros 
arquivos em Python para acessar a função readJsonFile.

"""

""" criação do programa principal
Você criará o programa principal que analisa os 
dados JSON e calcula o peso molecular, como no laboratório anterior.
Primeiro, importe o módulo jsonFileHandle. Abra 
o arquivo calc_weight_json.py e adicione o seguinte:"""

