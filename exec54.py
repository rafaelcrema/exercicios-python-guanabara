'''
crie um programa que leia o ano de nascimento de sete pessoas e 
mostre quantas já tem mais de 18 e quantas não tem
'''
from datetime import date

print('==='*15)
print('EXERCICIOS 54'.center(45))
print('==='*15)
print(' ')

ano_atual = date.today().year
anos = []
anos_maior = []
anos_menor = []

for i in range(1, 8):
    anos_digitados = int(input('Digite o ano de nascimento:\n>'))
    anos.append(anos_digitados)

for c in anos:
    idade = ano_atual - c

    if idade >= 18:
        anos_maior.append(c)
    else:
        anos_menor.append(c)

print(f'Temos {len(anos_maior)} pessoas maiores de idade\n{anos_maior}')
print(f'Temos {len(anos_menor)} pessoas menores de idade\n{anos_menor}')


