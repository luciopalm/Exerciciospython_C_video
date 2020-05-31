import datetime
ano = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - ano
if idade <= 9:
    print('Categoria MIRIM')
elif 9 < idade <= 14:
    print('Categoria INFANTIL')
elif 14 < idade <= 19:
    print('Categoria JUNIOR')
elif 19 < idade <= 20:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')
