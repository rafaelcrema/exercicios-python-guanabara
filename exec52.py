'''
FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO
'''


print('==='*15)
print('EXERCICIOS 52'.center(45))
print('==='*15)
print(' ')

total_dividido = 0

num = int(input('Digite um número inteiro: \n>'))

for i in range(1, num +1):
    if num % i == 0:
        total_dividido += 1

print(f'O número foi diviaivel {total_dividido} vezes.')

if total_dividido == 2:
    print(f'Por isso ele é primo')
else:
    print(f'Por isso ele não é primo')
