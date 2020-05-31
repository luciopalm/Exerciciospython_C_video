resp = 'S'
media = quant = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('QUER CONTINUAR?? [S/N] :')).upper().strip()[0]
media = soma / quant
print('Vc digitou {} numeros e a media foi {}'.format(quant, media))
print('O maior numero digitado foi {} e o menor foi {}'.format(maior, menor))
