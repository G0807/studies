lista = []
distancia = (input('Digite a distância da sua viagem:')).lower().split('k')
lista = distancia
valor = float(lista[0])
if valor <= 200:
    print(f'O valor da passagem é R${valor * 0.50:.2f}')
else:
    print(f'O valor da passagem é R${valor * 0.45:.2f}')


