n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
if m < 5:
    print('Sua média foi {} pontos. você foi reprovado.'.format(m))
elif m >= 7:
    print('Sua média foi {} pontos. você foi aprovado!'.format(m))
else:
    print('Sua média foi {} ponto. Você está de recuperação!'.format(m))