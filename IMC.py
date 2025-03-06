peso = input('Digite seu peso. Kg:').strip(' ').replace(',','.')
altura = input('Digite sua altura. mts: ').strip(' ').replace(',','.')
peso_float = float(peso)
altura_float = float(altura)

imc = peso_float / altura_float ** 2
print(f'Seu indice de massa corpórea é: {imc:.2f}')
if imc < 18.5:
    print('Você esta abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você esta no peso ideal!')
elif imc > 25 and imc <= 30:
    print('Você esta com sobre peso!')
elif imc > 30 and imc <= 40:
    print('Você esta obeso!')
elif imc > 40:
    print('Você esta com obesidade mórbida!')
    