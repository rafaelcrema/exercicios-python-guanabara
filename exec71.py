'''
CRIE UM FUNCIONAMENTO DE UM CAIXA ELETRONICO. NO INICIO, PERGUNTE O USUARIO QUAL SERA O VALOR A SER SACADO
E O PROGRAMA VAI NIFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES.

OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE:
R$50,00
R$20,00
R$10,00
R$1,00
'''

print('==='*15)
print('EXERCICIOS 70'.center(45))
print('==='*15)
print(' ')

print("="*12)
print("BANCO")
print("="*12)
print()

import random

lista_dinheiro = [50, 20, 10, 1]
cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1= 0

valor_sacar = int(input('Quanto você quer sacar? '))

while True:

    cedula = random.choice(lista_dinheiro)

    if cedula <= valor_sacar:
        valor_sacar -= cedula

        if cedula == 50:
            cedula50 += 1

        elif cedula == 20:
                cedula20 += 1

        elif cedula == 10:
                cedula10 += 1

        elif cedula == 1:
                cedula1 += 1


print(f'Você sacou {cedula50} cedulas de R$50,00')
print(f'Você sacou {cedula20} cedulas de R$20,00')
print(f'Você sacou {cedula10} cedulas de R$10,00')
print(f'Você sacou {cedula1} cedulas de R$1,00')

'''for cedulas in lista_dinheiro:
    quantidade = valor_sacar // cedulas

if quantidade > 0:
    print(f'{quantidade} de cedulas de R${cedulas}')

valor_sacar = valor_sacar % cedulas'''