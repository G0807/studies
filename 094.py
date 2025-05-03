'''094'''
lista = []
idade = []
mulheres = []
media = []
base = {}
fim = 'FIM'
while True:
	base['nome:'] = input('Nome: ').strip(' ').capitalize()
	base['idade'] = int(input('Idade: '))
	base['sexo'] = input('Sexo,[M/F]:').strip(' ').upper()
	lista.append(base.copy())
	idade.append(base['idade'])
	if 'F' in base['sexo']:
		mulheres.append(base['nome:'])		
	fim = input('Para encerrar digite "Fim".').strip(' ').upper()
	if fim == 'FIM':
		break
media = sum(idade) / len(lista)			
print(f'Quantidade  de pessoas cadastradas {len(lista)}.')	
print(f'A média de idade é: {sum(idade) / len(lista):.2f} ')
print(f'Mulheres cadastradas: {mulheres}')
print('Pessoa(as) com idade acima da média: ')
for d in lista:
	if d['idade'] > media:
		print(d)