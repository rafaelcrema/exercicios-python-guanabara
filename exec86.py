'''
crie um programa que crie uma matriz de dimensao 3x3 e preencha com
valores lidos pelo teclado
'''

print('==='*15)
print('EXERCICIOS 86'.center(45))
print('==='*15)
print(' ')

matriz = list()
matriz1 = list()
matriz2 = list()
matriz3 = list()

for m in range(3):
    m1 = int(input(f'Digite um valor para a posição 0,{m}: '))
    matriz1.append(m1)

for m in range(3):
    m2 = int(input(f'Digite um valor para a posição 1,{m}: '))
    matriz2.append(m2)

for m in range(3):
    m3 = int(input(f'Digite um valor para a posição 2,{m}: '))
    matriz3.append(m3)

matriz.append(matriz1)
matriz.append(matriz2)
matriz.append(matriz3)

for n in matriz:
    for n0 in n:
        print(f'[{n0}]',end='')
    print()