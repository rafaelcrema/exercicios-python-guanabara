'''
FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO MULTIPLOS DE
3 E QUE SE ENCONTRAM ENTRE 1 A 500
'''

print('==='*15)
print('EXERCICIOS 48'.center(45))
print('==='*15)
print(' ')

for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        print(n)