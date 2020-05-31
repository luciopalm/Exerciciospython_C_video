import math
an = float(input('digite o angulo que vc deseja:'))
seno = math.sin(math.radians(an))
cose = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print('o seno do angulo vale: {} \n o coseno do angulo vale: {} \n a tangente do angulo vale: {}'.format(seno, cose, tang))
