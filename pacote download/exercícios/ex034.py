s = float(input('Qual é o seu salário? '))
if s > 1250:
    a = (s*(10/100))
    sa = (a + s)
else:
    a = (s*(15/100))
    sa = (a + s)
print('seu aumento é de R${} e o seu salário vai para R${}'.format(a,sa))