
n = int(input('Digite um número para calcular seu fatorial:'))
c = n
f = 1
print(f'Calculando{n}!=')
while c > 0 :
    print (f'{c}', end=' ')
    print(' x ' if c > 1 else '=', end=' ')
print(f'{f}')
#    