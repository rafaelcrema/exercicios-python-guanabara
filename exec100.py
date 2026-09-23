'''
FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR()
A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NUMEROS E VAI COLOCALOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO 
VAI MOSTRAR OS NÚMEROS PARES SORTEADOS PELA FUNÇÃO ANTERIOR
'''

print('==='*15)
print('EXERCICIOS 100'.center(44))
print('==='*15)
print(' ')

import random
from time import sleep

def sorteia(num):
    for sorteia in num:
        lista_numeros.append(sorteia)

    for n in lista_numeros:
        print(f'\033[32m{n}\033[m',end=' ', flush=True)
        sleep(0.2)

    print(f'\nA lista sorteda é: \033[32m{lista_numeros}\033[m')

def somapar():
    for par in lista_numeros:
        if par % 2 == 0:
            lista_par.append(par)
    
    print(f'\nA lista par é \033[32m{lista_par}\033[m')
    soma = sum(lista_par)
    print(f'A soma dos pares são: \033[32m{soma}\033[m')


lista_numeros = []
lista_par = []
sorteia(random.sample(range(0,100),random.randint(1,20)))
somapar()
