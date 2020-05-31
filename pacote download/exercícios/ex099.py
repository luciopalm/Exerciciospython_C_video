from time import sleep


def maior(*num):
    cont = maior = 0
    print('\nAnalizando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor foi {maior}')

maior(2, 9, 5, 7, 9, 0)
maior(4, 7, 9)
maior(1, 2)
maior(6)
maior()