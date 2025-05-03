'''104
Esta função tem o objetivo de coletar valores int
do usuario, garantindo que o valor será int. '''
#def leia_int():
 #   while True:
  #      try:
   #         numero = int(input('Digite um numero inteiro:'))
    #        break
     #   except ValueError:
      #      print()
       #     print('Digite um valor valido!')
#leia_int()
#leia_int()
# O codigo abaixo é uma versão alternativa sem o uso de try, except.
def leia_int(msg):
    ok = False
    valor = 0
    while True:
        numero = input(msg)
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

numero = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {numero}.')
        


                
