'''Exercício 065.'''
resposta = 'S'
cont = 0
cont2 = 1
media = 0
soma = 0
soma2 = 0
fim = 1
print('Digite os números que deseja obter a média da sua soma, para encerrar digite 0.\n')

while fim != 0:
    num = int(input(f'{cont + 1}º número.'))
    soma += num
    cont += 1
    if num == 0:
         break
    
print(f'A média da soma dos números é {soma /(cont - 1):.2f}')    


resposta = input('Você quer continuar? Digite S para sim e N para encerrar.').upper()
if resposta == 'S':
     
     while fim != 0:
          num2 = int(input(f'{cont2}º número.'))
          soma2 += num2
          cont2 +=1

          if num2  == 0:
               break
elif resposta != 'S':          
   print('Fim.')
print(f'A soma de todos os números é {soma + soma2}')             
print(f'A a media adicionando os novos números é {(soma2 + soma) / ( cont2):.2f}')
                        



