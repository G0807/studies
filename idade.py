#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
ano = datetime.now()
ano = ano.year
print(ano)
lista = []
for i in range(1,4):
    ano_nasc = int(input(f'Digite o {i}º ano de nascimento: '))
result = ano - ano_nasc
print(result)
if result < 18:
    lista.append(ano_nasc)
    print(lista)


