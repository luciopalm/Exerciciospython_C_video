def area(lar, com):
    a = lar * com
    print(f'A área de um terreno {lar}x{com} é de {a}m²')


def titulo():
    print('CONTROLE DE TERRENOS')
    print('-'*20)


titulo()
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
area(lar, com)
