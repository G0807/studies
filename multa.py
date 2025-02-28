lista = []
velocidade = input('Digite a velicidade do veículo:').lower().split('k')
lista = velocidade
numero = float(lista[0])
if numero > 80:
    print(f'Você foi multado em R${(numero - 80) * 7:.2f}')
else:
    print('Parabens! Você esta dentro do limite de velocidade')
    #S
