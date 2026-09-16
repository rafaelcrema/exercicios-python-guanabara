'''
APRIMORE O DESAFIO 93.
PARA QUE ELE FUNCIONE COM VARIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO DE CADA JOGADOR
'''

print('==='*15)
print('EXERCICIOS 95'.center(45))
print('==='*15)
print(' ')

atletas = {}
codigo = 0
total = {}

while True:
    #CADASTRAR NOVO JOGADOR
    atleta = {}
    gols = []

    nome = input('Digite o nome do jogador: ').strip().capitalize()
    partidas = int(input(f'Quantas partidas o {nome} jogou? '))

    for g in range(partidas):
        n_gols = int(input(f'Quantos Gols o {nome} fez na partida {g+1}: '))
        gols.append(n_gols)

    sum_gols = sum(gols)
    med_gols = sum_gols / partidas

    atleta['nome'] = nome
    atleta['Partidas'] = partidas
    atleta['Gols'] = gols
    atleta['Total'] = sum_gols
    atleta['Média de gols'] = med_gols

    atletas[codigo] = atleta.copy()
    codigo += 1

    while True:
        add_cadastro = input('Quer adicionar mais um atleta? [S/N]').strip().upper()
        if add_cadastro in ('S', 'N'):
            print('=-='*30)
            break
        else:
            print('Resposta incorreta! Tente novamente')
    if add_cadastro == 'N':
        break

#ANALIZA JOGADOR

print()
print(f'{'COD':<10}|{'NOME':^20}|{'JOGOS':>10}')
print('-'*42)
for cod, jogador in atletas.items():
    print(f'{cod:<10}{jogador['nome']:^20}{jogador['Partidas']:>10}')

while True:
    selecao = int(input('Selecione o número do jogador para analizar: '))

    print(f'{selecao} | {atletas[selecao]['nome']}')
    print('-=-'*30)
    print(f'Gols feitos: {atletas[selecao]['Gols']} | Média de gol por partida: {atletas[selecao]['Média de gols']}')
    print('-=-'*30)

    #FIM DO CODIG
    while True:
        coninuar = input('Quer continuar verificando? [S/N]').strip().upper()
        if coninuar in ('S','N'):
            break
        else:
            print('Resposta errada, tente novamente!')

    if coninuar == 'N':
        break
    else:
        print()
        print(f'{'COD':<10}|{'NOME':^20}|{'JOGOS':>10}')
        print('-'*42)
        for cod, jogador in atletas.items():
            print(f'{cod:<10}{jogador['nome']:^20}{jogador['Partidas']:>10}')
        print('-'*42)
