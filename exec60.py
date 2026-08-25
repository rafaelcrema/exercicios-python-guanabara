'''
FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL
'''

print('==='*15)
print('EXERCICIOS 60'.center(45))
print('==='*15)
print(' ')

fatorial = 1
list_fatorail = []

num = int(input('Digite o número para descobrir o fatorial: '))

contador = num

while contador > 0:
    fatorial *= contador
    contador -= 1
    list_fatorail.append(fatorial)

print(f'A lista é {list_fatorail}')
print(f'O fatorial é: \033[32m{fatorial}\033[m]')
