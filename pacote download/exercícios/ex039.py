import datetime
ano = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - ano

if idade < 18:
    f = 18 - idade
    print('Voce ainda vai se alistar, faltam {} anos para o alistamento'.format(f))
elif idade > 18:
    f = idade - 18
    print('Voce ja passou do prazo para alistamento em {} anos'.format(f))
else:
    print('Está na hora de se alistar!')
