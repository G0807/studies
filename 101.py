'''101'''
from datetime import datetime

def analizador(a=0,b=0,c=0):
	a = 'não possui titúlo de eleitor.'
	b = 'possui titúlo de eleitor, voto obrigatório.'
	c = 'voto opcional.'
	if idade < 18:
		return a
	elif idade > 18 and idade < 65:
		return b
	else:
		return c
	

data = datetime.now().year	
ano = int(input('Ano de nascimento:'))
idade = data - ano
print(f'{idade} anos, {analizador()}')	