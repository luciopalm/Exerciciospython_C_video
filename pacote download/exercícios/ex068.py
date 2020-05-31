from random import randint
c = randint(0, 10)
cont = 0
camp = 0
while True:
    j = int(input('Jogue um numero: '))
    esc = str(input('PAR OU IMPAR? [P/I] ')).strip()
    s = c + j
    if s % 2 == 0:
        if esc in 'Pp':
            print(f'voce jogou {j} e o computador jogou {c}. O total deu PAR')
            print(f'Você VENCEU!!!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print(f'voce jogou {j} e o computador jogou {c}. O total deu PAR')
            camp = c
    else:
        if esc in 'Ii':
            print(f'voce jogou {j} e o computador jogou {c}. O total deu IMPAR')
            print(f'Você VENCEU!!!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print(f'voce jogou {j} e o computador jogou {c}. O total deu IMPAR')
            camp = c

    if camp == c:
        break
print('')
print('=*'*20)
print('VOCE PERDEU')
print(f'Nº de vitorias:{cont}')
print('=*'*20)


