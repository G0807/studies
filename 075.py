'''Exrcício 075'''
counter = 0
tuple_value = ()
even = ()

for number in range(1,5):
    counter += 1
    value = int(input(f'Digite o {number}º valor:'))
    tuple_value += (value,)
    if value % 2 != 0:  
        counter -= 1
    if value % 2 == 0:  
        even += (value,)
print(tuple_value)
print(f' Quantos números 9 --> {tuple_value.count(9)}.')
if 3 in tuple_value:
    print(f'A primera vez que aparece o número 3 é na {tuple_value.index(3) + 1}ª posição.')
else:
    print('Não há ocorrencias do numero 3.')

print(f'{counter}- pares digitados.--> {even}')


