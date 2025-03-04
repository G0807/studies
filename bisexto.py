ano = int(input('Digite que quer analisar:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bisexto')
else:
    print('O ano não é bisexto')
    
