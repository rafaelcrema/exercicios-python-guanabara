'''
FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VAOR DIGITADO PELO USUARIO
O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO
'''

print('==='*15)
print('EXERCICIOS 67'.center(45))
print('==='*15)
print(' ')

while True:
    tab = int(input('Digite o número da Tabuada que vocês quer ver: \n>'))
    print(f'A tabuada de \033[36m{tab}\033[m é:')
    for i in range(1, 11):
        valor = i * tab
        print(f'\033[34m{i}\033[m x \033[36m{tab}\033[m = \033[32m{valor}\033[m')

    cond = input('Quer continuar vendo outras Tabuadas? \033[36m[S/N]\033[m').strip().upper()

    if cond == 'N':
        break
    elif cond != 'S' or cond != 'N':
        print('Opção invalida')
    else:
        continue
