primeiro = int(input('primeiro termo: '))
razao = int(input('Razão: '))
d = primeiro + (10 - 1) * razao
for c in range(primeiro, d + razao, razao):
    print('{} '.format(c), end=' > ')
print('ACABOU')

