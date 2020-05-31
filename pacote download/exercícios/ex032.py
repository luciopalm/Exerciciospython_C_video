from datetime import date
ano = int(input('Que ano? coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é BISEXTO'.format(ano))
else:
    print('{} não é bisexto'.format(ano))