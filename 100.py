'''100'''
from random import randint
numeros = []
par = []
soma = 0
def sorteio():
  for n in range(1, 6):
    num = randint(1,5)
    numeros.append(num)
  print(f'Os números sorteados foram: {numeros}')
  
def somapar():
  for n in numeros:
    if n % 2 == 0:
      par.append(n)
  print(f'A soma dos pares é: {sum(par)}')

sorteio()
print()
somapar()

