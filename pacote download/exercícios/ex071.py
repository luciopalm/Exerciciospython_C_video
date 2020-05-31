lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu comi {comida}')
print('Comi q so a porra')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')


for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


