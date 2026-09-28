'''
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA()
QUE RECEBE DOIS PARAMENTROS OPCIONAIS: NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU.

O PRAGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FUCA DO JOGADOR, MESMO QUE ALGUUM DADO 
NÃO TENHA SIDO INFORMADO CORRETAMENTE
'''

print('==='*15)
print('EXERCICIOS 103'.center(44))
print('==='*15)
print(' ')

#FUNÇÃO
def ficha(n = ' ', gol = 0):
    n = nome
    gol = gols

    print('---'*20)
    if n == '':
        print(f'O jogador null marcou {gol} gols')
    elif gol == 0:
        print(f'O jogaror {n} marcou 0 gols')
    elif n == '' and gol == 0:
        print(f'O jogaro null, marcou 0 jogos')
    else:
        print(f'O jogador {n}, marcou {gol} gols')


#CONDIGO PRINCIPAL
nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ')

ficha()