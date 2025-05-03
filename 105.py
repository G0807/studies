def notas_alunos():
  print(ficha)
  if situação == 'SIM':
   print(f' {ficha['Situação da Turma']}')

nomes = []
counter = 0
notas = []
ficha = {}
situação = ' '
while True:
	counter += 1
	aluno = input(f'Digite o nome do {counter}º aluno: ').strip(' ').lower().capitalize()
	nomes.append(aluno)
	fim = input('Para cadastrar outro aluno digite Enter\nPara cadastra notas digite Fim.').strip(' ').upper()
	if fim == 'FIM':
		break

for n in nomes:
    while True:
        try:
            nota = int(input(f"Digite a nota do aluno {n} (Somente números inteiros): "))
            notas.append(nota)
            break
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")
print(notas)
maior = max(notas)
menor = min(notas)
media = sum(notas)//len(nomes)


ficha['Nome:'] = nomes
ficha['Notas:'] = notas
ficha['Maior Nota:'] = maior
ficha['Menor Nota:'] = menor
situação = input('Para ver a situação da Turma digite Sim: ').strip(' ').upper()
if situação == 'SIM':
  if media < 5:
    situação = 'Turma abaixo da média!'
  elif media == 5:
    situação = 'Turma na média!'  
  elif media > 5:
   situação = 'Turma acima da media!'
   ficha['Situação da Turma'] = situação
notas_alunos()