valores = list()
maior = menor = 0

for count in range(0, 6):
    valores.append(int(input(f'Digite um numero para a posição {count}: ')))
    if count == 0:
        maior = menor = valores[count]
    else:
        if valores[count] > maior:
            maior = valores[count]
        if valores[count] < menor:
            menor = valores[count]
print(f'Vc digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end='')




