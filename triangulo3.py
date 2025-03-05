reta1 = int(input('Digite o valor do primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta:'))
reta3 = int(input('Digite o valor da terceira reta:'))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Estas retas formam um triângulo.')
    if reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
        print('Um triângulo Equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Um triângulo Isóceles.')
    else:
        print('Um triângulo Escaleno.')            
else:
    print('Estas retas não formam um triâgulo!')