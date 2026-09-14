'''
CRIE UM PROGRAMA ONDE 4 JOGADORES JOGAM UM DADO E TENHAM RESULTADOS ALEATORIOS.
GUARDE ESSES RESULTADOS EM UM DICIONARIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO DO DADO
'''

print('==='*15)
print('EXERCICIOS 91'.center(45))
print('==='*15)
print(' ')

import random
import time

num_dado = {}

for n in range(4):
    dado = random.randint(1,6)
    print(f'O jogador {n +1} tirou: {dado}')
    num_dado[n] = dado
    time.sleep(1)

ordenado = sorted(
    num_dado.items(),
    key= lambda item: item[1],
    reverse=True
)
print('-='*20)
for p,d in ordenado:
    print(f'O jogador {p+1} tirou {d}')
    time.sleep(1)

