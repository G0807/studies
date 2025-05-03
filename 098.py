'''098'''
from time import sleep
a = int(input('Início:'))
b = int(input('Fim:'))
c = int(input('Internalo:'))
if c == 0:
   print('Intervalo invalido valor 1 adicionado')
   c = 1
if a < b and c > 0:
   b += 1
elif a > b and c < 0:
    b -= 1
print(b)    
for i in range(a, b, c):
   print(f'{i}',end=' ',flush=True)
   sleep(1)

