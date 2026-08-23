'''
faça um programa que leia o peso de 5 pessoas.
no final, mostre qual foi o maior e o menor peso lido
'''
from datetime import date

print('==='*15)
print('EXERCICIOS 55'.center(45))
print('==='*15)
print(' ')

lista_pesos = []

for n in range(1, 6):
    peso = float(input('Digite seu peso: \n>'))
    lista_pesos.append(peso)

maior_peso = max(lista_pesos)
menor_peso = min(lista_pesos)

print(f'O maior peso é {maior_peso}')
print(f'O menor peso é {menor_peso}')