cateto_op = float(input('Digite o valor do cateto oposto:'))
cateto_adj = float(input('Digite o valor do cateto adjacente:'))
hipotenusa = (cateto_op**2 + cateto_adj**2)**(1/2)
print(f'O valor da hipotenusa é {hipotenusa:.2f}')
#
import math
hipotenusa = math.hypot(cateto_op, cateto_adj)
print(f'O valor da hipotenusa é {hipotenusa:.2f}')
#
