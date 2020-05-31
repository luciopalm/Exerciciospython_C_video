lista = list()

while True:
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N]: '))
    lista.append(n)
    if r in 'Nn':
        break
if 5 in lista:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor 5 não está na lista')
print(f'Foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f'a lista ordenada em ordem decrescente é {lista}')
