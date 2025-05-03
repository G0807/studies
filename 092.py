'''092'''
import datetime
data_atual = datetime.datetime.now()
idade = 0
maior_idade = 0
aposentadoria = []
base = {}
base['nome'] = input('Digite seu nome:')
base['ano de nascimento'] = int(input('Digite o ano do seu nascimento:'))
print(base)
ano = base['ano de nascimento']
maior_idade = data_atual.year - ano
if maior_idade > 18:
    base['numero_carteira'] = int(input('Número da Carteira de Trabalho :'))
    base['ano_contratação'] = int(input('Ano da 1ª contratação :'))
    base['1º salario'] = input('Seu primeiro salário: ')
    anocontrataçao = base['ano_contratação']
    ano = anocontrataçao + 35 - data_atual.year
    base['aposentadoria'] = data_atual.year + ano
    print(f'Faltam {ano} para aposentar.')
    print(base)
else:
    idade2 = ano + 18 - data_atual.year
    print(f'Ainda faltam {idade2} para maior idade.')    


