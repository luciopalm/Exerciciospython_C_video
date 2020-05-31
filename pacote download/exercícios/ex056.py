somaidade = 0
maioridade = 0
maioridadehomem = 0
nomevelho = ''
menormulheres = 0
for p in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {} pessoa: '.format(p)))
    sexo = str(input('Qual o sexo da {}ª pessoa (M/F): '.format(p))).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        menormulheres += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é {} anos'.format(mediaidade))
print('O homem mais velha se chama {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('NA lista tem {} mulheres menores de 20 anos'.format(menormulheres))
