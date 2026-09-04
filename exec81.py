'''
CRIE UM PROGRAMA QUE VAI LER VARIOS NÚMRTOD E COLOCAR EM UMA LISTA
DEPOIS DISSO, MOSTRE
[A] QUANTOS NÚMEROS FORAM DIGITADOS
[B]A LISTA DE VALORES ORDENADOS DE FORMA DECRESCENTE
[C]SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA
'''

print('==='*15)
print('EXERCICIOS 81'.center(45))
print('==='*15)
print(' ')

lista_num = []
while True:
    valor = int(input('Digite um número: '))
    lista_num.append(valor)

    escolha = input('Quer digitar mais números? [S/N]').strip().upper()
    if escolha == 'N':
        break

decrescente = sorted(lista_num, reverse=True)
print(f"Existem \033[32m{len(lista_num)}\033[m números na lista!")
print(f'A lista em ondem descrescente é:\n\033[32m{decrescente}\033[m')

if 5 in lista_num:
    posicao = lista_num.index(5)
    print(f"O número 5 esta na posição \033[32m{posicao}\033[m")

else:
    print('Não ten número 5 na lista!')

