'''Exercício 085'''
base = []
list_even = []
list_odd = []
for i in range(1,8):
	numbers = int(input(f'Digite o  número:'))
	if numbers % 2 == 0:
		list_even.append(numbers)
		list_even.sort()
	if numbers % 2 != 0:
		list_odd.append(numbers)
		list_odd.sort()
base.append(list_even[:])
base.append(list_odd[:])
print(base)
print(f'Lista de números pares {list_even}\nLista de números ímpares {list_odd}')