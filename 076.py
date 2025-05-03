'''Exercício 076'''

goods = ('lapis','R$2,00','caderno','R$35,00','regua','R$3,00','mochila','R$75,00')

for i in range(0, len(goods),2):
    print(f'*{goods[i]:<10}----------{'':->4}{goods[i + 1]:<10}')