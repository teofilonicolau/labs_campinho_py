# atribuição de variáveis, listas e dicionários
#No painel de navegação do IDE, escolha o arquivo 
#criado na seção Criação do arquivo de exercício em Python anterior.
# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

#Na próxima linha, crie um dicionário inserindo: 
#pKR = {'y': 10.07,}

#Para preencher o dicionário com pares de chave-valor, 
# insira a primeira chave de y com um valor de 10.07. 
# Coloque o cursor dentro das chaves e insira: 'y': 10.07,

pKR = {'y': 10.07,'c': 8.18,
'k': 10.53,
'h': 6.00,
'r': 12.48,
'd': 3.65,
'e': 4.25}

#Observação: a vírgula inserida após o valor serve para adicionar os pares de chave-valor restantes.

#Adicione os pares de chave-valor a seguir no dicionário para corresponder ao segmento do código.

#Neste exercício, você usará o método count() e a compreensão da lista 
# para contar o número de aminoácidos 
# Y, C, K, H, R, D e E. Esses aminoácidos contribuem para a carga líquida.

#Para identificar a contagem de um item dentro de uma lista, 
# você pode usar o método count(). 
# Para ver quantos aminoácidos presentes na insulina são Y, 
# use o método count() inserindo: insulin.count("Y")

insulin.count("Y")

#Em seguida, atualize a linha 
# insulin.count() convertendo a variável 
# retornada pelo método count() para um float: float(insulin.count("Y"))

float(insulin.count("Y"))

#Agora que você tem a base para identificar uma única entidade, você 
# pode usar esse método para encontrar todas as entidades de uma lista.
#  Esse processo pode ser feito usando a compreensão da lista.
#  Para toda a linha, insira: seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

#Neste exercício, 
#você criará a fórmula da carga líquida. Você usará a 
#variável netCharge fornecida em uma fórmula de carga 
#líquida baseada em Python. A função da fórmula inclui um loop 
#while que exibirá a carga líquida enquanto a variável pH for igual ou inferior a 14.Crie uma variável chamada pH e inicialize-a para zero inserindo pH = 0 e pressionando ENTER.

#Crie o loop while inserindo while (pH <= 14): e pressionando ENTER.
#Copie a variável netCharge a seguir e cole-a no início do loop while.

pH = 0 

(pH <= 14)

netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))

#Para imprimir a variável netCharge com o pH, use 
# uma string de formato para melhor legibilidade. 
# Insira print('{0:.2f}'.format(pH), netCharge) e pressione ENTER.

print('{0:.2f}'.format(pH), netCharge)

#Finalmente, incremente a variável pH inserindo pH +=1 e pressionando ENTER.

pH +=1
















