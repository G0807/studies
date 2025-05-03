from meu_pacote.moedas.aumentar import aumentar
from meu_pacote.moedas.metade import metade
from meu_pacote.moedas.dobro import dobro

p = float(input('Digite um preço: '))
print(f'{p} aumentado em 10% é {aumentar(p)} ')
print(f'A metade de {p} é {metade(p)} ')
print(f'O dobro de {p} é {dobro(p)} ')
