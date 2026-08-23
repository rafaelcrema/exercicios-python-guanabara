'''
REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE NÚMERO QUE O USUARIO ESCOLHE, SÓ  QUE AGORA
COM FOR
'''


print('==='*15)
print('EXERCICIOS 49'.center(45))
print('TABUADA'.center(45))
print('==='*15)
print(' ')

n = int(input('Escolha o número que você quer fazer a tabuada: \n>'))

for i in range(0, 11):
    result = n * i
    print(f'A tabuada de {n} é {n} x {i} = {result}')
