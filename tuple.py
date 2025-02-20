# Exemplo de uso de tuplas
tuple1 = (1,2,3,4,5)
#         0 1 2 3 4
tuple2 = (6,7,8,9,10)
#
tuple3 = tuple1 + tuple2
print(tuple3)
# Acessando elementos da tupla
print(tuple3[3])
# Acessando intervalos da tupla
print(tuple3[3:8])
# Aqui ele pegará do numero 4 até o 8
print(tuple3[3:])
# Aqui ele pegará do numero 4 até o final
print(tuple3[:5])
# Aqui ele pegará a metade da tupla
print(tuple3[:])
# Aqui ele pegará a tupla inteira
print(tuple3[-1])
# Aqui ele pegará o ultimo elemento da tupla
print(tuple3[-2])
# Aqui ele pegará o penultimo elemento da tupla


