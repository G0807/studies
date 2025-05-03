'''103'''
#def ficha(jogador=0, gols=0):
#    print(f"FICHA DO JOGADOR ")
#    print(f"Nome do jogador: {jogador} ")
#    print(f"Número de gols: {gols} ")

#esta funçao mostra a ficha mesmo 
#que falte dados.(nome so jogador e
#gols marcados).

#jogador = input('Digite o nome do jogador: ')
#gols = input('Digite a quantidade de gols marcados: ')
#ficha(jogador, gols)
def ficha(jogador='<Desconhecido>',gols=0):
    print(f'Jogador {jogador} fez {gols} gol(s).')

nomejog = input('Digite o nome do jogador:')
numgols = input('Digite o números de gols:')

if numgols.isnumeric():
    numgols = int(numgols)
else:
    numgols = 0
if nomejog.strip() == '':
    nomejog = ficha(gols=numgols)
else:
    ficha(nomejog, numgols)   
