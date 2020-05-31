n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
if n1 > n2 and n1 > n3:
    print('{} é o maior'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é maior'.format(n2))
else:
    print('{} é maior'.format(n3))