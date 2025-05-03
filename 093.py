'''093'''
base = {}
counter = 0
total_gol = []
base['nome'] = input('Nome do jogador: ').strip(' ').capitalize()
base['numero_partidas'] = int(input('Número de partidas jogadas: '))
for p in range(1,base['numero_partidas'] + 1):
	gol = int(input(f'Quantidade de gol na {p}ª patida: '))
	total_gol.append(gol)
	total = sum(total_gol)
base['total de gols'] = total
base['media de gols'] = base['total de gols'] / base['numero_partidas']
print('='*30,'\nPlayer Stats')	
for k, v in base.items():
	print(f'{k}---> {v}')
#resolver problema de diminuir casas decimais da media de gols
	