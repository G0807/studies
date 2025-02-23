numero = int(input ('Digite um número:' ))
print(f'Tabuada do {numero}:' )
for i in range(1,11):
    print(f'{numero} x {i:2} = {numero * i}')
    