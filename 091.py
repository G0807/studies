'''091'''
from time import sleep 
from random import randint
base = {'jogador1':0,'jogador2':0,'jogador3':0,'jogador4':0}
lista = []
counter = 0
for j in range(1,5):
  counter += 1
  result = randint(1,6)
  lista.append(result)
base['jogador1'] = lista[0]
base['jogador2'] = lista[1]
base['jogador3'] = lista[2]
base['jogador4'] = lista[3]
base2 = dict(sorted(base.items()))
for k, v in base2.items(): 
    print(f'{k}--->{v}pontos')
    sleep(2)
maior = max(base2, key=base2.get)
maiorponto = max(base2.values())
print(f'O vencedor foi {maior} com {maiorponto} pontos.')
