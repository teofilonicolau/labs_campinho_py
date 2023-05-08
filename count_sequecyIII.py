#Salve os aminoácidos 90-110 no arquivo ainsulin-seq-clean.txt. Verifique se seu arquivo tem 21 caracteres
#Neste programa, usamos a indexação de strings para obter a sequência 
#de caracteres da posição 89 à posição 110 (novamente, lembre-se de que 
#a indexação em Python começa em 0). A expressão string[89:110+1] 
#retorna os caracteres da posição 89 até a posição 110 da string, 
#que correspondem à sequência solicitada. Em seguida, usamos a 
#função len() para contar o número de caracteres na sequência resultante e 
#imprimimos o resultado. Finalmente, usamos a função print() para imprimir a sequência de caracteres resultante.

string = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
sequencia = string[89:110+1]
contagem = len(sequencia)
print("O número de caracteres da posição 90 à posição 110 é:", contagem)
print("A sequência de caracteres da posição 90 à posição 110 é:", sequencia)


