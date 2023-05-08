# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:


#Nome da variável String para salvar na variável

lsInsulin = "malwmrllpllallalwgpdpaaa"

bInsulin  = "fvnqhlcgshlvealylvcgergffytpkt"

aInsulin  =  "giveqcctsicslyqlenycn"

cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"


insulin = bInsulin + aInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:

print("The sequence of human preproinsulin:")

print("The sequence of human insulin, chain a:", aInsulin)


#Neste laboratório, você calculará o peso molecular da insulina, com o qual você trabalhará em laboratórios posteriores.





# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

#. Você usará elementos desse código para trabalhar com loops e funções em outros laboratórios
#então veja como o código está escrito e tente seguir o resultado esperado.

#o peso molecular real da insulina humana é 5807,63. Porém, o programa informa 6696,42 
#porque ignora certas ligações e o processamento pós-tradução. Para calcular a 
#porcentagem de erro:error percentage = (| measured – accepted | / accepted)*100%


molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))




