'''Aula 17'''
num = [2,5,9,1]
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2,0)
print(num)
num.pop(2)
print(num)
print(len(num))
print('--------------------------------')
valores = []
valores.append(1)
valores.append(2)
valores.append(3)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('---------------------------------')
cont = 0
valor = []
for i in range(0, 4):
    cont += 1
    val = int(input(f'Digite o {cont}º número:'))
    valor.append(val)
for a, b in enumerate(valor):
    print(f'Na posição {a} encontrei o valor {b}')
    






