'''Exercício 070'''

gastototal = 0
cont = 0 
produto1000 = 1000.0
nomeproduto = ' '
soma = 0
menorpreço = 0

while True:
    produdos = input('Digite o nome do produto:').strip().upper()
    preço = input('Digite o preço do produto R$:')
    preço = preço.replace('.', '')
    preço = preço.replace(',', '.')
    preço_float = float(preço)
    
    cont += 1
    soma += preço_float
    if cont == 1:
        menor = preço
        barato = produdos
    else:
        if preço_float < menor:
            menor = preço_float
            barato = produdos     
    
    if preço_float < produto1000:
        cont -=1

    if preço_float <= preço_float:
        menorpreço += preço_float 

    fim = input('Você quer continuar? Digite "S" para sim, ou qualquer tecla para encerrar.').strip().upper()     
    if fim == "S":
        continue
    else:
        break
print(f'A quantidade de produtos acima de R$ 1.000,00, é -->{cont}')

print(f'A soma de todos produtos é --> {soma} ')
print(f'{barato} é o produto mais barato.')

