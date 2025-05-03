'''Exercício 073'''
position = ('1º Botafogo','2° Palmeiras',' 3º Flamengo','4º Fortaleza',
            '5º Internacional','6º São Paulo','7º Corinthians',
            '8º Bahia','9º Cruzeiro','10º Vasco','11º Vitória',
            '12º Atlético MG','13º Fluminense','14º Gremio',
            '15º Juventude','16º Red Bull','17º Athletico-PR',
            '18º Criciúma','19º Atlético-GO','20º Cuiabá')

print(f'Lista de Times do Brasileirão 2024 {position}\n') 
print('--*--'*20)
print(f'Os 5 primeiros são:{position[:5]}')
print('--*--'*20)
print(f'Os 4 útimos são: {position[-4:]}')
print('--*--'*20)
clear = tuple(' '.join(time.split()[1:]).strip() for time in position)
alphabet = tuple(sorted(clear))
print(f'Os times em ordem alfabética:{alphabet}')
print('--*--'*20)
print(f'Em {position[7]}')