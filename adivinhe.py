import random
print('Adivinhe o número de 0 a 5. Qual número estou pensando? ')
numero  = [1, 2, 3, 4, 5]
sorte = random.choice(numero)
while True:
    resposta = int(input( 'Digite o número que estou pensando:'))
    if resposta == sorte:
        print('Você acertou!')
        break
    else:
        print('Você errou! Tente novamente.')
        #fim

