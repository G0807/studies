numero = int(input('Digite um número: '))
opcao = input('Escolha a opção de converção numerica que você deseja.\
\nDigite: 1 para número binário.\nDigite: 2 para número octal\nDigite: 3 para hexadecimal.\nOpção: ').strip(' ')
binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexa = hex(numero)[2:]
if opcao == '1':
    print(f'O número covertido para binário é:{binario}')
elif opcao == '2':
    print(f'O númera convertido para octal é:{octal}')
elif opcao == '3':
    print(f'O número convertido para hexadecimal é:{hexa}')
else:
    print('Opção invalida!')            
#fim