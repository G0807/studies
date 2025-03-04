r1 = int(input('primeiro segmento:'))
r2 = int(input('segundo segmento:'))
r3 = int(input('terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um tiângulo')
    