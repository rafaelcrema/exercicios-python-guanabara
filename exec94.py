'''
CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VARIAS PESSOAS, 
GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONARIO E TODOS OS DICIONARIOS EM UMA LISTA.
NO FINAL, MOSTRE
[A] QUANTAS PESSOAS FORAM CADASTRADAS
[B]A MÉDIA DE IDADE DO GRUPO
[C]UMA LISTA COM TODOS AS MULHERES.
[D]UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA
'''

print('==='*15)
print('EXERCICIOS 94'.center(45))
print('==='*15)
print(' ')

grupo_pessoas = {'Pessoas': []}
pessoa = []
med = []
mulheres = []
acima_med = []

while True:
    nome = input('Nome: ').strip().capitalize()

    while True:
        sexo = input('Sexo: [M/F]: ').strip().upper()
        if sexo in ('M', 'F'):
            break
        else:
            print('Resposta errada, tente novamente!')

    idade = int(input('Idade: '))

    pessoa.append(nome)
    pessoa.append(sexo)
    pessoa.append(idade)

    med.append(idade)
    total_idade = sum(med)

    grupo_pessoas['Pessoas'].append(pessoa[:])
    pessoa.clear()

    if sexo == 'F':
        mulheres.append(nome[:])

    while True:
        coninuar = input('Quer continuar? [S/N]').strip().upper()
        if coninuar in ('S','N'):
            break
        else:
            print('Resposta errada, tente novamente!')

    if coninuar == 'N':
        break

quant = len(grupo_pessoas['Pessoas'])

med_idade = sum(med) / quant

for pessoa in grupo_pessoas['Pessoas']:
    if pessoa[2] > med_idade:
        acima_med.append(pessoa[0])

print('-=-'*30)
print(grupo_pessoas)
print('-=-'*30)
print(f'=> Foram cadastradas {quant} pessoas')
print(f'=> A idade média é de {med_idade}')
print(f'=> As mulheres dastradas foram: \n{mulheres}')
print(f'=> As pessoas acima da média de idade são: \n{acima_med}')
   