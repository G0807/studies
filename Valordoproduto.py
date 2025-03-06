produto = input('Qual o valor do produto? R$:').strip(' ').replace(',','.')
opcao = input('Qual a forma de pagamento?\n"Digite"\n1.Dinheiro a vista.\n2.Catão avista\n3.2x no catão\n4.3x ou mais no cartão.\n"Opção":')
produto_float = float(produto)
if opcao == '1':
    print(f'O valor à vista no dinheiro fica R${produto_float - produto_float * 0.10:.2f}')
elif opcao == '2':
    print(f'O valor à vista no cartão é R${produto_float - produto_float * 0.05:.2f}')
elif opcao == '3':
    print(f'O valor parcelado em 2x no cartão é R${produto_float:.2f}')
elif opcao == '4':
    print(f'O valor parcelado em 3x ou mais no cartão é R${produto_float + produto_float * 0.20:.2f}')

