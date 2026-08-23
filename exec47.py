'''
CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS PARES QUE ESTÃO ENTRE 1 E 50
'''

print('==='*15)
print('EXERCICIOS 47'.center(45))
print('==='*15)


for n in range(1, 51):
    if n % 2 == 0:
        print(n)