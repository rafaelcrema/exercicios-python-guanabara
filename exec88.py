'''
FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIA PALPITE.
O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS E VAI SORTEAR 6 DIGITOS ENTRE 1 E 60 PARA CADA JOGO, CADASTRADO TUDO EM
UMA LISTA COMPOSTA
'''

print('==='*15)
print('EXERCICIOS 88'.center(45))
print('==='*15)
print(' ')

import time
import random

print("-=-=-=-=-=-=-=-=-=-=-=-=")
print('-=-= Mega da Virada -=-=')
print('-=-=-=-=-=-=-=-=-=-=-=-=')
print()

lista_mega = []


escolha_jogos = int(input('Quantos jogos vocês quer gerar? '))

for e in range(escolha_jogos):
   
   jogos = []

   while len(jogos) < 6:
      num_sorteado = random.randint(0, 60)

      if num_sorteado not in jogos:
        jogos.append(num_sorteado)

   lista_mega.append(jogos)
   print(f'Jogo {e + 1}: {sorted(jogos)}')
   time.sleep(0.5)
