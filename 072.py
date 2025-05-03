# aula 16 exemplos
#lanche = ('hanburgue', 'suco', 'pizza', 'pudim')
#print(lanche[-1])
#for comida in lanche:
    #print(f'eu comi {comida}')

#for cont in range(0, len(lanche)):
    #print(f'comi {lanche[cont]}')
#---------------------------------------
'''Exercícios 072'''
written = ('Zero','Um','Dois','Três','Quatro',
           'Cinco','Seis','Sete','Oito','Nove','Dez')
while True:
    enter = int(input('Digite um número de 0 a 10:'))
    
    if enter < 0 or  enter > 10:
        print('Opção invalida!')
        continue
    else:
        print(f'Você digitou o número "{written[enter]}."')
        break

