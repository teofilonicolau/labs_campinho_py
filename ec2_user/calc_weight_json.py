#Primeiro, importe o módulo jsonFileHandle. Abra o arquivo calc_weight_json.py e adicione o seguinte:

import jsonFileHandler 

#Recupere os dados JSON e armazene-os em uma variável data.
#quase nao consigo por conta do caminho
data = jsonFileHandler.readJsonFile("C:\\Users\\Samsung\\Desktop\\campinhoDigital\\pythonCampinho\\ec2-user\\insulin.json")


#Teste se os dados retornados não estão vazios e obtenha os dados da insulina.

"""if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")
"""

"""Também é possível testar o que acontece se o arquivo não é encontrado. 
Por exemplo, altere o nome do arquivo para 'files/insuline.json' e execute o 
programa. Você receberá a seguinte mensagem:
Could not read file
Error. Exiting program
Desfaça a última alteração para que o 
arquivo volte a ter o nome files/insulin.json.
Na seção if do código, abaixo do último print, adicione o seguinte código:
""" 

if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")
# Calculating the molecular weight of insulin  
# Getting a list of the amino acid (AA) weights  
aaWeights = data['weights']
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))
print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
