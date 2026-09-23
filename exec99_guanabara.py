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

def maior(* num):
    print('Os numeros analizados são:...')
    cont = maior = 0
    for valor in num:
        for c in valor:
            print(f'{c}', end=' ')
            if c > maior:
                maior = c
            cont +=1
    print(f'\nForam informados {cont} valores')
    print(f'O maior valor é: {maior}\n')

cont_novo = 0
num_gerados = random.randint(1,10)
while cont_novo < num_gerados:
    maior(random.sample(range(0,100),random.randint(0,10)))
    sleep(1)
    cont_novo +=1

print(f'Foram analizados {cont_novo} seguencias')
