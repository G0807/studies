'''aula 20'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
f1 = fatorial(5)
print(f'O fatorial de 5 é: {fatorial(5)}')    