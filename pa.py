'''Progressão Aritmética'''

termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a Razão:'))
decimo = termo + (10 - 1) * razao

for p in range(termo,decimo + razao, razao,):
    print(p,end=' ')