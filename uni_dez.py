numero = int(input('Digite um número:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')

