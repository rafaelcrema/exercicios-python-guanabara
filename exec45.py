'''
CRIE UM JOKENPÔ
'''

import random

print('''
==========================================
            EXERCICIO 45
              JOKENPÔ
==========================================               
''')
print(' ')

start = input('''


     ██╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗██████╗  ██████╗
     ██║██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔══██╗██╔═══██╗
     ██║██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██████╔╝██║   ██║
██   ██║██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██╔═══╝ ██║   ██║
╚█████╔╝╚██████╔╝██║  ██╗███████╗██║ ╚████║██║     ╚██████╔╝
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝      ╚═════╝


              >>> APERTE 1 PARA COMEÇAR <<<
''')

if start == '1':
  contador = 0

  pontuação_jogador = 0
  pontuação_CPU = 0


  while contador < 5:
    escolha_jogada = input('''
[1] PEDRA
[2] PAPEL
[3] TESOURA
''')
    jogada_CPU = random.randint(1, 3)

    #LOGICA DO JOGO
    if escolha_jogada == '1' and jogada_CPU == 2:
      jogada_CPU = 'PAPEL'
      escolha_jogada = 'PEDRA'
      pontuação_CPU = pontuação_CPU + 1
      print('Você perdeu a rodada. Você escolheu {} e a CPU escolheu {}\nPontuação Jogador: {}\npontuação CPU: {}'.format(escolha_jogada, jogada_CPU,pontuação_jogador,pontuação_CPU))
      

    elif escolha_jogada == '1' and jogada_CPU == 3:
      jogada_CPU = 'TESOURA'
      escolha_jogada = 'PEDRA'
      pontuação_jogador = pontuação_jogador + 1
      print('Você ganhou a rodada. Você escolheu {} e a CPU escolheu {}\nPontuação Jogador: {}\npontuação CPU: {}'.format(escolha_jogada, jogada_CPU,pontuação_jogador,pontuação_CPU))
      

    elif escolha_jogada == '2' and jogada_CPU == 1:
      jogada_CPU = 'PEDRA'
      escolha_jogada = 'PAPEL'
      pontuação_jogador = pontuação_jogador + 1
      print('Você ganhou a rodada. Você escolheu {} e a CPU escolheu {}\nPontuação Jogador: {}\npontuação CPU: {}'.format(escolha_jogada, jogada_CPU,pontuação_jogador,pontuação_CPU))
      

    elif escolha_jogada == '2' and jogada_CPU == 3:
      jogada_CPU = 'TESOURA'
      escolha_jogada = 'PAPEL'
      pontuação_CPU = pontuação_CPU + 1
      print('Você perdeu a rodada. Você escolheu {} e a CPU escolheu {}\nPontuação Jogador: {}\npontuação CPU: {}'.format(escolha_jogada, jogada_CPU,pontuação_jogador,pontuação_CPU))
      

    elif escolha_jogada == '3' and jogada_CPU == 1:
      jogada_CPU = 'PEDRA'
      escolha_jogada = 'TESOURA'
      pontuação_CPU = pontuação_CPU + 1
      print('Você perdeu a rodada. Você escolheu {} e a CPU escolheu {}\nPontuação Jogador: {}\npontuação CPU: {}'.format(escolha_jogada, jogada_CPU,pontuação_jogador,pontuação_CPU))
      

    elif escolha_jogada == '3' and jogada_CPU == 2:
      jogada_CPU = 'PAPEL'
      escolha_jogada = 'TESOURA'
      pontuação_jogador = pontuação_jogador + 1
      print('Você ganhou a rodada. Você escolheu {} e a CPU escolheu {} \nPontuação Jogador: {}\npontuação CPU: {}'.format(escolha_jogada, jogada_CPU,pontuação_jogador,pontuação_CPU))
      

    else:
      print('Impatou.')

    contador = contador + 1


  if pontuação_jogador > pontuação_CPU:
    print('PARABÉNS!!! Você venceu')
  elif pontuação_jogador == pontuação_CPU:
    print('Empatou!!!')
  else:
    print('Sorry, você perdeu!')
    



else:
  print('Vaza daqui!!!!')