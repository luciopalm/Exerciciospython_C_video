pes = {}
pes['nome'] = str(input('Nome: '))
pes['media'] = float(input(f'Média de {pes["nome"]}: '))
if pes['media'] >= 7:
    pes['situação'] = 'Aprovado'
elif 5 <= pes['media'] < 7:
    pes['situação'] = 'Recuperação'
else:
    pes['situação'] = 'Reprovado'
print('-='*30)
for k, v in pes.items():
    print(f'{k} = {v}')



