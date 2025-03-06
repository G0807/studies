from datetime import datetime
ano_nasc = int(input('Digite o ano que você nasceu: '))
ano_atual = datetime.now()
ano_atual = ano_atual.year
maior_idade = ano_nasc + 18
result1 = ano_atual - maior_idade
if result1 > 0:
    print(f'Você esta atrasado {result1} anos, para seu alistamento militar ')
elif maior_idade > ano_atual:
    print(f'Ainda falta {maior_idade - ano_atual} anos para o seu alistamento militar.')
elif ano_nasc + 18 == ano_atual:
    print('Este ano é o ano do seu alistamento militar.')