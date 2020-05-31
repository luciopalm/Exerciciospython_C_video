n = cont = soma = 0
n = int(input('DIGITE UM NUMERO [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('DIGITE UM NUMERO [999 para parar]: '))
print('vc digitou {} numeros e a soma foi {}'.format(cont, soma))
