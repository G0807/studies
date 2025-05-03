'''Exercício 074'''
import random
neutral_tuple = ()
cont = 0
look = 0
while cont >= 0 and cont < 6:
    look = random.randint(0,20)
    cont += 1
    numbers=(look,)
    neutral_tuple = neutral_tuple + (numbers)
    if cont == 1:
        bigger = look
    else:
        if look > bigger:
            bigger = look
    if cont == 1:
        smaller = look
    else:
        if look < smaller:
            smaller = look        
print(neutral_tuple)
print(f'O mair número é: {bigger}')
print(f'O menor número é:{smaller}')

# Resolução Guanabara.

#from random import randint
#numeros = (randint(1,10)),randint(1,10)),randint(1,10)),randint(1,10)),randint(1,10)),randint(1,10)),
#print('Os valores sorteados foram: ', end='')
#for n in numeros:
    #print(f'{n} ', end='')
#print(f'\nO maior valor sorteado foi {max(numeros)}')
#print(f'O menor valor sorteado foi {min(numeros)}')
