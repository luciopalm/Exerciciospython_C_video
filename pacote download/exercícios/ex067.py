print('PROGRAMA TABUADA')
c = 0
while True:
    n = int(input('Digite um numero positivo para ver a tabuada ou um negativo para finalizar: '))
    if n <= 0:
        break
    for c in range(1,11):
        prod = n * c
        print(f'{n} x {c} = {prod}')
print('OBRIGADO POR USAR A TABUADA, VOLTE SEMPRE COMPANHEIRO')
