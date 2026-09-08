'''
FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VARIAS PESSOAS, GUARDE TUDO EM UMA LISTA.
NO FINAL, MOSTRE:
[A] QUANTAS PESSOAS FORAM CADASTRADAS
[B] UMA LISTA COM AS PESSOAS MAIS PESSADAS.
[C] UMA LISTAGEM COM AS PESSOAS MAIS LEVES.
'''

print('==='*15)
print('EXERCICIOS 84'.center(45))
print('==='*15)
print(' ')

pessoas = list()
dados = list()
mais_pesadas = list()
menos_pesadas = list()

while True:
    nome = input("Qual o nome: ").capitalize()
    dados.append(nome)
    peso = float(input('Peso: '))
    dados.append(peso)
    pessoas.append(dados[:])
    if peso <= 70:
        menos_pesadas.append(dados[:])

    else:
        mais_pesadas.append(dados[:])
    dados.clear()

    opcao = input('Quer continuar? [S/N]').strip().upper()
    if opcao == 'N':
        break

print(f'O total de pessoas cadastras foram: \033[32m{len(pessoas)}\033[m')

print('As pessoas menos pesadas são: ')
for n,p in menos_pesadas:
    print(f'{n:<15} | {p:>10}kg ',end=' \n')

print('=-'*15)

print(f'As pessoas mais pesadas são:')
for n1,p1 in mais_pesadas:
    print(f'{n1:<15} | {p1:>10}kg ',end=' \n')
    