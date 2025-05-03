'''Exercício 079'''
counter = 0
counter = 0
list1 = []
answer = ('S','N')
while True:
	counter += 1
	numbers = int(input(f'Digite o {counter}º número:'))
	list1.append(numbers)
	if list1.count(numbers) > 1:
		print('Número duplicado, não foi adcionado a lista')	
	answer = str(input('Você quer continuar? [S/N]')).upper()
	if answer != 'S':
		break
print('Sua lista é', set(list1))