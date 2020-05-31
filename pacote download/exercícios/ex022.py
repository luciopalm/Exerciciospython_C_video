nome = str(input('Digite seu nome completo:')).strip()
mai = nome.upper()
min = nome.lower()
print('Maiúsculas : {}'.format(mai))
print('Minusculas: {}'.format(min))
print('numero total de letras: {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))





