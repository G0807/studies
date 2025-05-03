'''Exercício 087'''
counter = 0
list1 = []
list2 = []
list3 = []
list4 = []
base = []
while True:
	counter += 1
	date = int(input(f'Digite o {counter}º número: '))
	if date % 2 == 0:
		list4.append(date)
	if counter < 4:
		list1.append(date)
	if counter > 3 and counter < 7:
		list2.append(date)
	if counter > 6 and counter < 10:
		list3.append(date)
	if counter >= 9:
		break
base.append(list1[:])
base.append(list2[:])
base.append(list3[:])
print(f'{base[0]}\n{base[1]}\n{base[2]}')
result = sum(list4) 
print(f' A soma dos números pares digitados é {result}.')
print('  A soma da coluna 3 é',(base[2][2] + base[1][2] + base[0][2]))
print(f' O maior numero da segunda linha é ',max(list2) )