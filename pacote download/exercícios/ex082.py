lista = []
par = []
impar = []
while True:
    n = int(input('Digite um numero: '))
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Nn':
        break
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Os valores pares são {par} e os valoes impares são {impar}')
print(f'A lista completa é {lista}')
