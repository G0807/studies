'''90'''
base = {}
base['nome'] = input('Digite o nome do aluno:').strip(' ').upper()
base['media'] = float(input('Digite a média do aluno:'))
if base['media'] >= 5:
	base['situação'] = 'aprovado'
else:
	base['situação'] = 'reprovado'	

print(base)


print(f'Aluno {base['nome']}\nMédia {base['media']}\nSituação: {base['situação']}')