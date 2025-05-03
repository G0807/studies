'''Exercício 081'''
list1 = []
counter = 0
answer = 'S','N'
while True:
	counter += 1
	number = int(input(f'Digite o {counter}º número:'))
	list1.append(number)
	answer = str(input('Você quer continuar? [S/N]')).upper()
	if answer != 'S':
		break
print(f'Sua lista tem {len(list1)} itens.')
reverse = sorted(list1, reverse = True)
print(f'Em ordem decrescente {reverse}')
if 5 in list1:
    print('O número 5 esta na lista.')
else:
    print('O número 5 não esta na lista.')