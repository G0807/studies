salario_m = float(input('Digite o salário do mês: '))
salario_anual = salario_m * 12
print ('O salário anual é R${:.2f}'.format(salario_anual))
print ('############################################')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
soma = n1 + n2
subtracao = n1 - n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
expo = n1 ** n2
print ('A soma é:{}\nA subtração é:{}\nA multiplicação é:{}\nA divisão é:{:.3f}\nA divisão inteira é:{}\nA exponenciação é:{}'.format(soma,subtracao,mult,div,div_int,expo))