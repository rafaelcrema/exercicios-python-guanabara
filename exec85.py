'''
CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR SETE VALORES NUMERICOS E CADASTREOS EM UMA LISTA UNICA
QUE MANTENHA SEPARADOS OS VALORES PARES E IMPARES.
NO FINAL, MOSTRE OS VLAORES PARES E IMPARES EM ORDEM CRESCENTE
'''

print('==='*15)
print('EXERCICIOS 85'.center(45))
print('==='*15)
print(' ')

num = list()
par = list()
impar = list()

for n in range(7):
    nf = int(input(f'Digite um número {n + 1}: '))
    if nf % 2 == 0:
        par.append(nf)
    else:
        impar.append(nf)

num.append(par)
num.append(impar)

print(f'Os números pares são: \033[32m{sorted(par)}\033[m')
print(f'Os números impares são: \033[32m{sorted(impar)}\033[m')