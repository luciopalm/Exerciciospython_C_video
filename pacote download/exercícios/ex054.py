import datetime
atual = datetime.date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    n = int(input('Digite o ano do nascimento da {}ª pessoa: '.format(pess)))
    idade = atual - n
    if idade >= 21:
        totmaior +=1
    else:
        totmenor +=1
print('Na lista tem {} pessoas maiores de idade e {} pessoas menores de idade.'.format(totmaior, totmenor))
