'''
CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VARIAS PESSOAS, 
GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONARIO E TODOS OS DICIONARIOS EM UMA LISTA.
NO FINAL, MOSTRE
[A] QUANTAS PESSOAS FORAM CADASTRADAS
[B]A MÉDIA DE IDADE DO GRUPO
[C]UMA LISTA COM TODOS AS MULHERES.
[D]UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA
'''

print('==='*30)
print('EXERCICIOS 94 COM LISTA DE DICIONARIOS'.center(45))
print('==='*30)
print(' ')
soma = media = 0

galera = []
pessoa = {}

mulheres = []
acima_media = []

while True:
#LIMPA A LISTA TODA VEZ QUE O WHILE RODA
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).capitalize()

    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if pessoa['Sexo'] in ('M','F'):
            break
        print('Erro! Por favor, digite apenas M ou F.')

#VERIFICA SE É MULHER, SE SIM, JOGA EM UMA LISTA MULHERES
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])

    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']

#FAZ UMA COPIA DA LISTA, PARA NÃO PERDER AO LIMPAR
    galera.append(pessoa.copy())

#PERGUNTA DE CONTINUAÇÃO DE CADASTRO
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in ('S','N'):
            break
        print('Erro! Por favor, digite apenas S ou N.')

    if resp == 'N':
        break

#EXIBE TOTAL DE PESSOAS CADASTRADAS
print('-='*30)
print(f'Foram cadastradas {len(galera)} pessoas!')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')

#EXIBE TODAS AS MULHERES CADASTRADAS
print('-='*30)
print('As mulheres são: ')
for mulher in mulheres:
    print(f'  => {mulher}')
print('-='*30)

#VERIFICA QUEM TEM IDADE ACIMA DA MÉDIA, JOGAS PARA LISTA ACIMA DA MÉDIA
if pessoa['Idade'] > media:
    acima_media.append(pessoa['Nome'])
print('As pessoas acima da média são:')
for pessoa in acima_media:
    print(f'  => {pessoa}')
