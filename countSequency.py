#Neste programa, usamos a indexação de strings novamente para obter as 
#letras da posição 24 à posição 53 (lembre-se de que a indexação em Python começa em 0). 
#A expressão string[24:54] retorna os caracteres da posição 24 até a posição 53 da string, 
#que correspondem às letras solicitadas. Em seguida, usamos a função len() para contar o
#número de caracteres na string resultante e imprimimos o resultado. 
#Finalmente, usamos a função print() para imprimir a sequência de caracteres resultante 
string = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
contagem = len(string[24:54])
print("O número de letras da posição 25 à posição 54 é:", contagem)
print("As letras da posição 25 à posição 54 são:", string[24:54])
