from random import randint
x = randint(1, 10)
resp = 11
t = 0
while resp != x:
    if resp != x:
        resp = int(input('Digite um número entre 1 a 10: '))
        print('Moiou, tente novamente')
        t += 1
print('PARABÉNS!!! VC ACERTOU!!!! PRECISOU DE {} TENTATIVAS'.format(t))