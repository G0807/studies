cit = input('Digite o nome de uma cidade:').lower()
print('santo' in cit)
#fim
frase = input('Digite uma frase:').lower().strip()

print(f'Há {frase.count("a")} letras "a" na frase')
print(f'A primeira letra "a" aparece na posição {frase.find("a")+1}')
print(f'A última letra "a" aparece na posição {frase.rfind("a")+1}')
#fim
nome =input('Digite seu nome completo:').strip()
print(f'Seu nome em maiúsculas é: {nome.upper()}\nSeu nome em minúsculas é: {nome.lower()}')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')
#fim
