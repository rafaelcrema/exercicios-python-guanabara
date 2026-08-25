'''
CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA

[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
'''
from math import prod

print('==='*15)
print('EXERCICIOS 59'.center(45))
print('==='*15)
print(' ')

codicao = 0
resul = 0
mais_num = []

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

while codicao == 0:

    cal = input('''
ESCOLHA UMA OPÇÃO:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
''')

    if cal == '1':
        resul = num1 + num2 + sum(mais_num)
        print(f'A soma entre os números {num1}, {num2} e números adicionados depois {mais_num} são: {resul}')

    elif cal == '2':
        resul = num1 * num2 * prod(mais_num)
        print(f'A multiplicação entre os números são: {resul}')

    elif cal == '3':
        if num1 > num2:
            print(f'O número {num1} é o maior')
        else:
            print(f'O número {num2} é maior')

    elif cal == '4':
        while cal == '4':
            num_nv = float(input('Digite um novo número: '))
            mais_num.append(num_nv)
            print(f'{mais_num}')

            nv_condicao = input('Quer digitar mais número? [S/N]').upper()
            if nv_condicao == 'S':
                continue
            else:
                cal = '9'

    elif cal == '5':
        break

    else:
        print('Opção errada, tente novamente.')
        continue   