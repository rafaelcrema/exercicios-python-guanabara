'''
faça um programa que jogue par ou impar com o computador.
O jogo só sera interrompido quando o jogador perder.
mostra o total de vitorias consecutivas que ele conquistou no final do jogo.
'''
from random import randint

print('==='*15)
print('EXERCICIOS 68'.center(45))
print('==='*15)
print(' ')

print("="*12)
print("Par ou Impar")
print("="*12)

contador = 0

while True:
    escolha = input('Escolhar PAR ou IMPAR: \n>').strip().upper()

    jogada_player = int(input('Escolha um número: \n'))

    cpu = randint(0,10)

    soma = jogada_player + cpu


    if soma % 2 == 0 and escolha == 'PAR':
        print(f'\033[32mParabéns, você ganhou!\033[m')
        print(f'Você jogou \033[32m{jogada_player}\033[m e a CPU jogou \033[31m{cpu}\033[m')
    elif soma % 2 == 0 and escolha == 'IMPAR':
        print(f'\033[31mVocê perdeu!\033[m')
        print(f'Você jogou \033[32m{jogada_player}\033[m e a CPU jogou \033[31m{cpu}\033[m')
        break
    if soma % 2 != 0 and escolha == 'PAR':
        print(f'\033[31mVocê perdeu!\033[m')
        print(f'Você jogou \033[32m{jogada_player}\033[m e a CPU jogou \033[31m{cpu}\033[m')
        break
    elif soma % 2 != 0 and escolha == 'IMPAR':
        print(f'\033[32mParabéns, você ganhou!\033[m')
        print(f'Você jogou \033[32m{jogada_player}\033[m e a CPU jogou \033[31m{cpu}\033[m')

    contador += 1

if contador > 1:
    print(f'Você ganhou \033[36m{contador}\033[m seguidas!')
else:
     print(f'Você ganhou \033[36m{contador}\033[m seguida!')