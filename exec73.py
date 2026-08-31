'''
CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLECAÇÃO.
DEPOIS MOSTRE:
[A] APENAS OS 5 PRIMEIROS COLOCADOS
[B] OS ULTIMOS 4 COLOCADOS
[C] UMA LISTA COM OS EM ORDEM ALFABETICA
[D] EM QUE POSIÇÃO BA TABELA ESTA O TIME DA CHAPECOENSE.
'''

print('==='*15)
print('EXERCICIOS 73'.center(45))
print('==='*15)
print(' ')

times = ('PALMEIRAS', 'FLAMENGO', 'ATHETICO-PR', 'FLUMINENSE', 'BAHIA', 'CRUZEIRO', 'ATLÉTICO-MG', 'BRAGANTINO',
        'CPRITIBA', 'CORINTHIANS', 'SÃO PAULO', 'BOTAFOGO', 'EC VITÓRIA', 'SANTOS', 'GRÉMIO', 'MIRASSOL',
        'VASCO DA GAMA', 'INTERNACIONAL', 'REMO', 'CHAPECOENSE')

#procurar posição do chapecoense
procura = 'CHAPECOENSE' 
for procura in times:
    posicao = times.index(procura)


print(f'Os 5 primeiros colocados são:\n\033[32m{times[0:5]}\033[m\n')
print(f'Os ultimos 4 times são:\n\033[31m{times[:-5: -1]}\033[m\n')
print(f'Em ordem alfabética, fica:\n \033[36m{sorted(times)}\033[m\n')
print(f'O Chapecoense está na posição: {posicao + 1}')