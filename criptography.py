"""Para iniciar o processo de implementação de uma 
cifra de César em Python, você criará uma função simples definida pelo usuário.
No painel de navegação do IDE, escolha o arquivo criado na seção Criação do a
rquivo de exercício em Python anterior.
Defina uma função chamada getDoubleAlphabet, 
que usa um argumento de string e concatena 
(ou combina) a string fornecida com ela mesma da seguinte forma:
Observação: as partes necessárias da declaração da função são 
a palavra-chave def, um nome e dois-pontos (:). Além disso, no Python, 
as variáveis não precisam ser declaradas, e os tipos de dados são 
inferidos a partir da declaração de atribuição"""

def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


"""A próxima função definida solicitará uma mensagem do 
usuário para ser criptografada. Você usará a função interna chamada input().
No editor de texto, insira o seguinte código e salve o arquivo:
Observação: as funções devem executar uma tarefa específica. 
Geralmente, como as funções realizam tarefas assim, elas provavelmente também serão curtas. 
Embora essa função retorne uma string, ela não usa um argumento, como a função getDoubleAlphabet()."""

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

""" obtenção de uma chave de cifra
A chave de cifra é o quanto você irá deslocar as 
letras. Usando dois alfabetos, você pode criar uma 
chave de cifra que é qualquer número inteiro de 1 a 25. 
Não conte a chave no índice 26, porque ela levaria 
você de volta para a mensagem original.
Defina uma função para solicitar uma chave de 
cifra do usuário inserindo o seguinte código:"""

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

"""criptografia de uma mensagem
Até agora, as funções foram curtas e simples. Esse é geralmente o caso quando você mantém uma tarefa específica dentro de uma função. A função encryptMessage será um pouco mais longa.

Antes de escrever o código, você deve planejar o algoritmo para criptografia da seguinte forma:
"""

"""Use três argumentos: a mensagem, a cipherKey (chave de cifra) e o alfabeto.

Inicialize as variáveis.

Use um loop for para percorrer cada letra na mensagem.

Encontre a posição de uma letra específica.

Determine a nova posição de uma letra específica, dada a chave de cifra.

Se a letra atual estiver no alfabeto, anexe a nova letra à mensagem criptografada.

Se a letra atual não estiver no alfabeto, anexe a letra atual.

Retorne a mensagem criptografada depois de esgotar todas as letras na mensagem.

No arquivo de exercício, insira o código a seguir e siga a lógica revisando as etapas do algoritmo anterior."""




def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

"""descriptografia de uma mensagem
Funções são úteis porque você pode reutilizá-las. 
Você escreverá uma função decryptMessage() reutilizando a 
função encryptMessage(). Para essa criptografia simples, 
você pode desfazer a criptografia mudando cada letra de volta. 
Logo, em vez de adicionar a chave de cifra, você subtrairá a chave.
 Para evitar reescrever a maior parte da lógica, basta passar uma chave de cifra negativa.
Depois, insira o seguinte código e salve o arquivo:"""



def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

"""criação de uma função principal
Você criou uma coleção de funções definidas pelo 
usuário que ajudarão você a escrever um programa 
com cifra de César. A lógica principal do programa 
será, naturalmente, contida em uma função também.
Antes de ir para o código, planeje a lógica:"""

"""Defina uma variável de string para conter o alfabeto inglês.

Para poder deslocar as letras, dobre sua string de alfabeto.

Receba uma mensagem do usuário para criptografar.

Obtenha uma chave de cifra do usuário.

Criptografe a mensagem.

Descriptografar a mensagem
Para ajudar na depuração e na compreensão do programa, 
foram adicionadas instruções print(), mas elas não são 
estritamente necessárias para o bom funcionamento do programa."""

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


"""Salve e execute o arquivo e, depois, veja os resultados.
Nada acontece. Por quê? Lembre-se de que uma função é uma 
seção nomeada de um programa que executa uma tarefa específica. Você não chamou sua função.
Para chamá-la, adicione a seguinte linha ao arquivo .py e salve o arquivo:"""
    
runCaesarCipherProgram()

    








