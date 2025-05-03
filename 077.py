'''Exercício 077'''
fruits = ('banana', 'uva', 'abacate', 'laranja')

vowels = "aeiouAEIOU"  # Lista de vogais (incluindo maiúsculas)
for word in fruits:
    # Filtrar as vogais presentes na palavra
    vowels_in_word = [letter for letter in word if letter in vowels]
    vowel_count = len(vowels_in_word)  # Contar quantas vogais existem
    unique_vowels = set(vowels_in_word)  # Obter as vogais únicas
    
    print(f"A palavra '{word}' tem {vowel_count} vogal(is): {', '.join(unique_vowels)}")
#Resolução Guanabara
#palavras = ('boi', 'vaca', 'cachorro', 'gato')
#for p in palavras:
    #print(f'\nNa palavra {p.upper()} temos', end='')
    #for letra in p:
        #if letra.lower() in 'aeiou':
            #print(letra, end='')
            