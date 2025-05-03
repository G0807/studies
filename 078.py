'''Exercício 078'''
counter = 0
answer = 'S','N'
list1 = []
while True:
    counter += 1
    number = int(input(f'Digite o {counter}° número:'))
    list1.append(number)
    answer = str(input('Quer continuar? [S/N]')).upper()
    if answer == 'S':
       continue
    else:
        break
print(list1) 
print(f'O maior valor da lista é:',max(list1),'e sua posição é:',list1.index(max(list1)))
print(f'O menor valor da lista é:',min(list1), 'e sua posição é :',list1.index(min(list1)))
