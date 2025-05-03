'''Exercício 82'''

list1 = []
list_impar = []
list_par = []
counter = 0
answer = 'S','N'
while True:
	counter += 1
	number = int(input(f'Digite o {counter}º número:'))
	list1.append(number)
	answer = str(input('Você quer continuar? [S/N]')).upper()
	if answer != 'S':
		break
		
print(f'A lista completa é {list1}')
for num in list1:
	if num % 2 == 0:
		list_par.append(num)
	else:
		list_impar.append(num)	
print(f'A lista de números pares é {list_par}')
print(f'A lista de impares é {list_impar}')
