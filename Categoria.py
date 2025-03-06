from datetime import datetime
ano_atual = datetime.now()
ano_atual = ano_atual.year
ano_nasc = int(input('Qual ano do seu nascimento?'))
if ano_atual - ano_nasc <= 9:
    print('Sua categoria é\33[3;32m MIRIM.')
elif ano_atual - ano_nasc > 9 and ano_atual - ano_nasc <= 14:
    print('Sua catigoria é\33[3;32m INFANTIL.')
elif ano_atual - ano_nasc > 14 and ano_atual - ano_nasc <= 19:
    print('Sua categoria é\33[3;32m JUNIOR.')
elif ano_atual - ano_nasc > 19 and ano_atual - ano_nasc <= 20:
    print('Sua categoria é\33[3;32m SÊNIOR.')
else:
    print('Sua categoria é\33[3;32m MASTER.')