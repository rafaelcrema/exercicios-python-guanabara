'''
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR()
QUE RECEBE VARIOS PARAMETROS COM VALORES INTEIROS.
SEU PROGRAMA TEM QUE ANALIZAR OS VALORES E DIZER QUAL DELES É MAIOR.
'''

print('==='*15)
print('EXERCICIOS 99'.center(45))
print('==='*15)
print(' ')

import random
from time import sleep

def maior():
    contador = 0
    while contador < 5:
        num_lista.clear()
        contador +=1
        num_maior = 0
        for r in random.sample(range(0,10),5):
            num_lista.append(r)
            if r > num_maior:
                num_maior = r

        num_lista.copy()

        for lista in num_lista:
            print(lista,end=' ',flush=True)
            sleep(0.2)
            
        print(f'\nO maior número é: \033[32m{num_maior}\033[m')
        print('---'*15)
        print('\n')



num_lista = []

maior()