n = (int(input('digite um numero: ')),
    int(input('digite um numero: ')),
    int(input('digite um numero: ')),
    int(input('digite um numero: ')))
print(f'Vc digitou os valores {n}')
print(f'O valor nove apareceu {n.count(9)} vezes')
if 3 in n:
    print((f'o valor 3 apareceu na {n.index(3)+1}ª posição'))
else:
    print('o valor nao foi digitado')
print('os valores pares digitados foram:')
for v in n:
    if v % 2 == 0:
        print(v, end='')
