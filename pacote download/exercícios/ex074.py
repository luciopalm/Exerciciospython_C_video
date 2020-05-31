from random import randint
tupla = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),randint(0, 10)
print('Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')



