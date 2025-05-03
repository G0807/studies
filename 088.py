'''088'''
import random
from time import sleep
counter = 0
saiz = 6
list2 = []
list1 = []
list3 =[]
game = int(input('Quantos jogos você quer fazer?'))
#Sorteando os numeros e colocando em uma lista de acordo com a quantidade de jogos.
while counter < game:
	counter += 1
	for i  in range(1,7):
		number = random.randint(1, 60)
		list1.append(number)
#Dividindo a lista em sub-listas.		
for iten in list1:
	list2.append(iten)
	if len(list2) == saiz:
		list3.append(list2)
		list2 = []
if list2:
	list3.append(list2)
print(list3)
for i, l in enumerate(list3):
	print(f'jogo{i+1}: {l}')
	sleep(2)
    
	