
'''Exercício 059.'''
somar = 1
multiplicar = 2
maior = 3
numnovo = 4
fim = 5
opçao = 0

num1 = int(input('Digite o 1º número:'))
num2 = int(input('Digite o 2º número:'))
print('O que você deseja fazer?\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do progama')
while opçao != 5:
	opçao = int(input('Digite sua opção: '))

	if opçao == 1:
		print(f'A soma de {num1} + {num2} = {num1 + num2}')

	elif opçao == 2:
		print(f'{num1} x {num2} = {num1 + num2}')
	elif opçao == 3:
		if num1 > num2:
			print(f'{num1} É o maior.')
		else:
			print(f'{num2} É o maior.')
	elif opçao == 4:
		novo1 = int(input('Dite 1º número:'))
		novo2 = int(input('Digite o 2º número:'))
		num1 = novo1
		num2 = novo2
if opçao == 5:
	print('Fim.')