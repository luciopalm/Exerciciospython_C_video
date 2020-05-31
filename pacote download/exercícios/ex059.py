n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero: '))
digit = 0
soma = 0
while digit != 5:
    print('')
    digit = int(input('''O QUE VC DESEJA FAZER COM ESSES NUMEROS? 
    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - MUDAR NUMEROS
    [5] - ENCERRAR
    
    '''))
    if digit == 1:
        soma = n1 + n2
        print('A SOMA É {}'.format(soma))
        print('')
    if digit == 2:
        mult = n1 * n2
        print('A MULTIPLICAÇÃO É {}'.format(mult))
        print('')
    if digit == 3:
        if n1 > n2:
            print('{} È MAIOR'.format(n1))
        else:
            print('{} É MAIOR'.format(n2))
    if digit == 4:
        n1 = int(input('DIGITE UM NUMERO: '))
        n2 = int(input('DIGITE OUTRO NUMERO:'))
print('=#=' * 10)
print('         TERMINATED')
print('=#=' * 10)
