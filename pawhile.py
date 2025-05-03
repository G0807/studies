# Definindo os parâmetros da progressão aritmética
inicio = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))   # Razão da progressão
termos = 10 # Número de termos

# Inicializando o contador e o termo atual
contador = 0
termo_atual = inicio

# Loop while para gerar a progressão aritmética
while contador < termos:
    print(f'{termo_atual}', end=' ')  # Exibe o termo atual antes de incrementar    
    termo_atual += razao
    contador += 1
print('FIM')



