'''106.
FUNÇÕES: ajuda() e msg(str)
ajuda()___auxilia usuari nas duvidas Python.
msg(str)___formata linhas ajustando automaticamente ao texto'''
import os
# Cores de texto ANSI
VERMELHO = '\033[91m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIANO = '\033[96m'
BRANCO = '\033[97m'
RESET = '\033[0m'  # Para resetar as cores ao padrão

# Cores de fundo ANSI
FUNDO_VERMELHO = '\033[41m'
FUNDO_VERDE = '\033[42m'
FUNDO_AMARELO = '\033[43m'
FUNDO_AZUL = '\033[44m'
FUNDO_MAGENTA = '\033[45m'
FUNDO_CIANO = '\033[46m'
FUNDO_BRANCO = '\033[47m'

def msg(str):
	lista = str
	print('=' * len(lista))
	print(str)
	print('=' * len(lista))


def ajuda():
  while True:
    função = input(VERMELHO + 'Digite qual função ou modolo quer receber ajuda:' + FUNDO_AZUL)
    print(f'{help(função)}')
    fim = input(FUNDO_VERMELHO + 'Digite fim para encerrar: ' + RESET).strip(' ').upper()
    if fim == 'FIM':
        break
  print(VERDE + 'FIM!' + RESET)  

msg(CIANO +'PYHELP---ASSISTENTE INTERATIVO.'+ RESET)
ajuda()