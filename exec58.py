'''
melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar. mostrando no final quantos palpites foram nescessarios para vender.
'''

print('==='*15)
print('EXERCICIOS 58'.center(45))
print('==='*15)
print(' ')

import random

#contador de palpites
palpite = 0
#random de escolha do pc
numero_pc = random.randint(1, 10)

#condição de repetição do while
escolha = -1

while escolha != numero_pc:

    escolha_jogador = int(input('Pense no número que eu pensei: '))

    if escolha_jogador == numero_pc:
        print(f'Você acertou! O número era \033[32m{numero_pc}\033[m')
    else:
        palpite +=1
        print('Você erro!')
        continue

    print(f'Número de palpites até o acerto: \033[31m{palpite}\033[m')