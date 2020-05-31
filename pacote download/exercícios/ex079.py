numeros = []
resp = 'S'

while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado, não vou adicionar')
    r = str(input('Quer continuar? [S/N] : '))
    if r in 'Nn':
        break
    if r not in 'Ss' and 'Nn':
        print('Erro de digitação. Digite S ou N')
numeros.sort()
print(f'Vc digitou os valores {numeros} ')

