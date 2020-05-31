s = 1
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo [F/M]: ')).upper()
    if s != 'M' and s != 'F':
        print('Erro de digitação, digite somente F ou M')
print('obrigado')