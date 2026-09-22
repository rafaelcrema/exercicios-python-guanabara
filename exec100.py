'''
FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR()
A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NUMEROS E VAI COLOCALOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO 
VAI MOSTRAR OS NÚMEROS PARES SORTEADOS PELA FUNÇÃO ANTERIOR
'''

print('==='*15)
print('EXERCICIOS 100'.center(45))
print('==='*15)
print(' ')

import random

lista_numeros = []
lista_par = []

def sorteia():
    for sorteia in random.sample(range(0,10),5):
        lista_numeros.append(sorteia)

    print(f'A lista sorteda é: \033[32m{lista_numeros}\033[m')

def somapar():
    for par in lista_numeros:
        if par % 2 == 0:
            lista_par.append(par)
    
    print(f'\nA lista par é \033[32m{lista_par}\033[m')
    soma = sum(lista_par)
    print(f'A foma dos pares são: \033[32m{soma}\033[m')

sorteia()
somapar()
