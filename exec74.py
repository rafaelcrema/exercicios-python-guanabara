'''
CRIE UM PROGRAMA QUE VAI GERAR 5 NUMEROS ALEATORIOS E COLOCAR RLR RM UMA TUPLA.
DEPOIS DISSO, MOSTRAR A LISTAGEM DE NÚEROS GERADO E TAMBÉM INDIQUE O MENOR E O MAIOR NÚMERO QUE ESTÃO NA TUPLA
'''

print('==='*15)
print('EXERCICIOS 74'.center(45))
print('==='*15)
print(' ')

import random

tuplas = ()

for i in range(5):
    tupla = random.randint(1, 10)
    tuplas = tuplas + (tupla,)

print(f'A tupla é: {tuplas}')
print(f'O menor número é: {sorted(tuplas)[0]}')
print(f'O maior número é: {sorted(tuplas)[4]}')




