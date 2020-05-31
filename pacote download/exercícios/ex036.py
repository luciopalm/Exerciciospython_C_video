casa = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
t = int(input('Em Quantos anos voce deseja pagar a casa?'))
pm = (casa / (t * 12))

if pm < sal * (30/100):
    print('A prestação mensal é de R${:.2f}'.format(pm))
else:
    print('O emprestimo foi negado!')
