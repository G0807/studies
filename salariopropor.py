salario = float(input('Digite seu salário '))
if salario >= 1250:
    print(f'Seu salário passa para {salario * 0.10 + salario}R$')
else:
    print(f'Seu salário passa para {salario * 0.15 + salario}R$')

