from math import hypot
cato = float(input('Digite o comprimento do cateto oposto:'))
cata = float(input('Digite o comprimento do cateto adjacente:'))
hip = hypot(cato,cata)
print('o valor da hipotenusa é {}'.format(hip))
