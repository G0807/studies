import random
resposta = input('Vamos jogar Jokem-Po? ').lower().strip(' ')
if resposta == 'sim':
    mao = input('O timo! Já escolhi minha mão! Digite a sua! pedra, papel ou tesoura?').lower().strip(' ')                                                                                              
else:
    print('Fica para próxima!')
mao_pc = ['pedra', 'papel', 'tesoura']
sorte = random.choice(mao_pc)
if  sorte == 'pedra' and mao == 'pedra':
       print('Empatamos!')
elif sorte == 'pedra' and mao == 'papel':
       print('Você venceu!')
elif sorte == 'pedra' and mao == 'tesoura':
    print('Você perdeu!')
elif sorte == 'papel' and mao == 'pedra':
        print('Você perdeu!')
elif sorte == 'papel' and mao == 'tesoura':
        print('Você venceu!')
elif sorte == 'papel' and mao == 'papel':
        print('Empatamos!')   
elif sorte == 'tesoura' and mao == 'pedra':
        print('Você venceu!')
elif sorte == 'tesoura' and mao == 'tesoura':
        print('Empatamos!')
elif sorte == 'tesoura' and mao == 'papel':
        print('Você venceu!')





