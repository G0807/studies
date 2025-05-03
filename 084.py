'''Exercício 084'''
base = []
date = []
lista3 = []
list4 = []
sn = 'S','N'
counter = 0
while True:
	counter += 1
	enter_name = input(f'Digite o {counter}º nome:  ').strip('')
	enter_kg = input(f'Digite o peso Kg:').replace(',','.')
	peso = float(enter_kg)
	date.append([enter_name,peso])
	sn = input('Quer continuar? [S/N]').strip('').upper()
	if sn == 'N':
		break
for item in date:
	lista3.append( item[0])
print(f'{counter} pessoas cadastradas, {lista3}')
print(f'A pessoas mais pesada é {max(date)},')
for peso in date:
	date.sort()
print(date)
print(f' As pessoas mais pesadas são, {date[-1],date[-2]}')
print(f' As pessoas mais leves são, {date[0],date[1]}')
