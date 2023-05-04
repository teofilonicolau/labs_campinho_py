import random

#Um loop whilefaz uma seção do código se repetir até que uma determinada 
# condição seja atendida. Neste exercício,
#  você criará um script Python que pede ao 
# usuário para adivinhar corretamente um número.

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Coloque o cursor na próxima linha após a segunda declaração print(). Depois, 
# insira uma declaração que gere um número aleatório entre 1 e 10 usando a 
# função randint()do módulo random.

number = random.randint(1,10)

#Verifique se o usuário adivinhou o número criando uma variável chamada isGuessRight :

isGuessRight = False

#Para lidar com a lógica do jogo, crie um loop while:

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

 #Use uma função print()para informar o usuário sobre o script:

print("Count to 10!")

#Observação: o Python usa recuos para saber se a declaração printestá dentro da declaração do loop for.

for x in range (0, 11):
    print(x)
    