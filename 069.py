'''Exercício 069'''
maioridade = 0
men = 0
mulher20 = 0
cont = 0
sexom = 0
sexof = 0

while True:
    idade = int(input('Idade:'))
    sexo = input('Sexo (M/F):').strip().upper()
    cont += 1
    if idade < 20 and sexo == 'F':
        mulher20 += 1
    if idade < 18:
        cont -= 1
    
    if sexo == 'M':
        
        sexom +=1
        
    if sexo == 'F':
            
        sexof += 1

    fim = input('Você quer continuar? Digite "S" para sim, ou qualquer tecla pra encerrar.').strip().upper()
    if fim == 'S':
        
        continue
    else:
        break
   
print(f'Quantidade de homens --> {sexom}.')

print(f'Quantidade de pessoas com mais de 18 anos --> {cont}.') 

print(f'Quantidade de mulheres com menos de 20 anos --> {mulher20}.')


