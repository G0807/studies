''' variaveis necessarias para interagir com as funções,todas com valores irrisórios, 
para poderem receber valores sem alterar o valor reebido'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
quantmulher = 0
'''Inicio do uso do '"for" com o intuito de altomatizar uma pesquisa'''
for p in range (1, 5):
    
    print(f'{p}ª Pessoa')
    nome = str(input('Nome:' )).strip()
    idade = int(input('Idade:' ))
    sexo = str(input('Sexo(M/F):' )).strip()
    '''coleta de daos terminada e inico da parte lógica para analize dos dados.'''
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        quantmulher += 1
        '''fim da analize dos dados '''
'''Por fim apresentação da analize dos dados coletados.'''
mediaidade = somaidade / 4
print(f'A média de idade do grupo de pessoas é:{mediaidade}')
print(f'O nome do homem mais velho é:{nomemaisvelho}')
print(f'Ao todo são {quantmulher} mulheres com menos de 20 anos.')
