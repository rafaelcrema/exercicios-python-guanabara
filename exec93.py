'''
CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTE DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR
E QUANTAS PARTIDAS ELE JOGOU.
DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA JOGO.
NO FINAL, TUDO ISSO SERA GUARDADO EM UM DICIONARIO, INCLUINDO O TOTAL DE HOLS FEITOS DURANTE O CAMPEONATO.
'''

print('==='*15)
print('EXERCICIOS 93'.center(45))
print('==='*15)
print(' ')

atleta = {}
gols = []
total = {}

nome = input('Digite o nome do jogador: ').strip().capitalize()
atleta['nome'] = nome

partidas = int(input(f'Quantas partidas o {nome} jogou? '))

for g in range(partidas):
    n_gols = int(input(f'Quantos Gols o {nome} fez na partida {g+1}: '))
    gols.append(n_gols)
atleta['Gols'] = gols

sum_gols = sum(gols)
atleta['Total'] = sum_gols

print('-=-'*20)
print(atleta)
print('-=-'*20)

print(f'O campo nome tem valor {atleta['nome']}')
print(f'O campo Gol tem o valor {atleta['Gols']}')
print(f'O campo Total tem valor {atleta['Total']}')

print('-=-'*20)

print(f'O jogador {atleta['nome']} jogou {partidas} partidas')
for jogo, gol in enumerate(atleta['Gols'], start=1):
    print(f'=> No jogo {jogo}, o {atleta['nome']} fez {gol} gols.')
