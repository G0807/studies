'''089'''
base = []
answer = 'S','N'
counter = 0
while True:
	counter += 1
	date_name = input(f'Digite o {counter}° aluno: ').upper()
	date_grade1 = input('Digite a nota:')
	date_grade2 = input('Digite a nota:')
	date_grade = date_grade1.replace(',','.')
	date_grade2 = date_grade2.replace(',','.')
	date_grade1 =  float(date_grade1,)
	date_grade2 =  float(date_grade2,)
	average = (date_grade1 + date_grade2)/2
	base.append([date_grade1,date_grade2,date_name,average])
	answer = input('Você quer continuar?[S/N]').strip(' ').upper() 
	if answer == 'N':
   		break	
print(base)
print('=' * 60)
print('='*2,'BOLETIM ESCOLAR','=' *2)
print(f'{'   [NOME':<5}---->{'MÉDIA]':>5}')
for i  in base:
	print(f'   [{i[2]:<5}--->{i[-1]:>5}]')
	