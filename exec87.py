'''
aprimore o desafio anterior, mostrando no final
[A]A SOMA DE TODOS OS VALORES PARES DIGITADOS
[B]A SOMA DE TODOS VALORES DA TERCEIRA FILEIRA
[C]O MAIOR VALOR DA SEGUNDA LINHA
'''

print('==='*15)
print('EXERCICIOS 87'.center(45))
print('==='*15)
print(' ')

matriz = list()
matriz0 = list()
matriz1 = list()
matriz2 = list()
matriz_par = list()

for m1 in range(3):
    mz0 = int(input(f'Digite o valor da matriz 0,{m1}: '))
    matriz0.append(mz0)
    if mz0 % 2 == 0:
        matriz_par.append(mz0)

for m2 in range(3):
    mz1 = int(input(f'Digite o valor da matriz 1,{m2}: '))
    matriz1.append(mz1)
    if mz1 % 2 == 0:
        matriz_par.append(mz1)

for m3 in range(3):
    mz2 = int(input(f'Digite o valor da matriz 2,{m3}: '))
    matriz2.append(mz2)
    if mz2 % 2 == 0:
        matriz_par.append(mz2)

matriz.append(matriz0)
matriz.append(matriz1)
matriz.append(matriz2)

print('-=-'*15)
for n in matriz:
    for nz in n:
        print(f'[{nz}]',end='')
    print()

sum_par = sum(matriz_par)
sum_terc = sum(matriz2)
maior = max(matriz1)

print('-=-'*15)
print(f'Os pares são:\n{matriz_par}')
print(f'A soma dos pares da: {sum_par}')
print('-=-'*15)
print(f'A soma da terceira fileira da matriz é: {sum_terc}')
print('-=-'*15)
print(f'O maior valor da segunda fileira da matriz é: {maior}')
print('-=-'*15)


