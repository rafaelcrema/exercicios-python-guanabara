'''
FAÇA UM PROGRAMA QUE LEIA 5 VALORES NÚMERICOS E GUARDEOS EM UMA LISTA
NO FINAL., MOSTRE QUAL O MAIOR E MENOR VALOR DIGITADO E AS SUS RESPCTIVES POSIÇÕES
'''

print('==='*15)
print('EXERCICIOS 78'.center(45))
print('==='*15)
print(' ')

lista_num = []

for n in range(5):
    num = int(input('Digite um número: '))
    lista_num.append(num)


menor_num = min(lista_num)
posicao_menor = lista_num.index(menor_num)

maior_mun = max(lista_num)
posicao_maior = lista_num.index(maior_mun)

print(lista_num)
print(f'O menor número é {menor_num} e sua posição é {posicao_menor}')
print(f'O maior número é {maior_mun} e sua posição é {posicao_maior}')
