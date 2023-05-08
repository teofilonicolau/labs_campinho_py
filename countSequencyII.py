#Salve os aminoácidos 55-89 no arquivo cinsulin-seq-clean.txt. Verifique se seu arquivo tem 35 caracteres.
##letras da posição 54 à posição 88 (lembre-se de que a indexação em Python começa em 0).
#Neste programa, usamos a indexação de strings para obter a sequência 
#de caracteres da posição 54 à posição 89 (novamente, lembre-se de que a indexação em Python começa em 0).
#A expressão string[54:89+1] retorna os caracteres da posição 54 até a posição 
#89 da string, que correspondem à sequência solicitada. Em seguida, 
#usamos a função len() para contar o número de caracteres na sequência resultante e 
#imprimimos o resultado. Finalmente, usamos a função print() para imprimir a sequência de caracteres resultante.

string = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
sequencia = string[54:89+1]
contagem = len(sequencia)
print("O número de caracteres da posição 55 à posição 89 é:", contagem)
print("A sequência de caracteres da posição 55 à posição 89 é:", sequencia)
