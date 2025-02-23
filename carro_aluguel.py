km_percorridos = float(input('Quantos km foram percorridos? '))
dias_alugados = int(input('Por quantos dias o carro foi alugado? '))
preço_total = (dias_alugados * 60) + (km_percorridos) * 0.15
print(f'O preço total a ser pago é de R${preço_total:.2f}')
