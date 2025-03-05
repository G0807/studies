casa_valor = float(input('Qual o valor da casa que deseja comprar? R$:'))
salario = float(input('Qual seu salário? R$:'))
anos = int(input('Enquantos anos você pretende pagar? Anos:'))
if casa_valor / (12 * anos) > salario * 0.30: 
    print('Sua compra não foi aprovada.')
else:
    print(f'Sua compra foi aprovada! Suas parcelas são de R${casa_valor/(12*anos):.2f}, mensais. ')


