'''
DESENVOLVA UM PROGRAMA QUE LEOA NOME, IDADE E SEXO DE 4 PESSOAS
NO FINAL, MOSTRE:
A MEDIA DE IDADE DO GRUPO
QUAL O NOME DO HOMEM MAIS VELHO
QUANTAS MULHERES TEM MENOS DE 20 ANOS
'''
from datetime import date

print('==='*15)
print('EXERCICIOS 56'.center(45))
print('==='*15)
print(' ')

lista_nome_m = []
lista_nome_f = []
lista_idade = []
total_mulher_20 = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''

for n in range(1, 5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [M/F]: ').strip().lower()[0]

    lista_idade.append(idade)

    if sexo == 'f'and idade < 20:
        total_mulher_20 += 1
    if sexo == 'm':
        lista_nome_m.append(nome)
    else:
        lista_nome_f.append(nome)

    if sexo == 'm':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome



media_idade = sum(lista_idade) / 4

print(f'A média de idade do Grupo é: {media_idade}')
print(f'O nome do homem mais velho é: {nome_homem_mais_velho}')
print(f'Existem {total_mulher_20} mulheres com menos de 20 anos na lista')

