# porção inteira de um número real
num = float(input('Digite um número real: '))
print(f'A porção inteira de {num} é {int(num)}')
# arredondamento de um número real
print(f'O número {num} arredondado é {round(num)}')
# arredondamento para cima
import math
print(f'O número {num} arredondado para cima é {math.ceil(num)}')
# arredondamento para baixo
print(f'O número {num} arredondado para baixo é {math.floor(num)}')


