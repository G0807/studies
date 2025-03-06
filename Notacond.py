nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Sua média é:{media}')
if media >= 7.0:
    print('Você foi aprovado!')
elif media < 5.0:
    print('Você foi reprovado!')
elif media >= 5.0 and media <= 6.9:
    print(' Você esta de recuperação!')
    