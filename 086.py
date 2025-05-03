'''Exercício 086'''
counter = 0
list1 = []
list2 = []
list3 = []
base = []
while True:
	counter += 1
	date = int(input(f'Digite o {counter}º número: '))
	if counter < 4:
		list1.append(date)
	if counter > 3 and counter < 7:
		list2.append(date)
	if counter > 6 and counter < 10:
		list3.append(date)
	if counter >= 9:
		break
base.append(list1)
base.append(list2)
base.append(list3)
print(base)
print('-'*30)
print(f'{base[0]}\n{base[1]}\n{base[2]}')


