'''Exercício 80'''
list1 = []
list2 = []
counter = 0
for number in range(1,6):
	number_list = int(input(f'Digite o {number}º número:'))
	list1.append(number_list)
	if number_list == min(list1):
		print('Este número será o primeiro da lista')
	elif number_list == max(list1):
		print('Este será o último número da lista.')
print(f'Esta é sua lista {list1}')
for i in range(1,6):
	counter += 1
	list2.append(min(list1))
	list1.remove(min(list1))
	 
	if counter == 5:
		list2 = list2
print(f'Esta é sua lista ordenada {list2}')
