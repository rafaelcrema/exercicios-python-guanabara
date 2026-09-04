'''
CRIE UM PROGRAMA QUE VAI LER VARIOS NÚMEROS E COLOCAR EM UMA LISTA
DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTAR APENAS NÚMEROS PARES E OS VALORES IMPARES DIGITADOS.

AO FINAL, MOSTRE O CONTEUDO DAS TRÊS LISTAS GERADAS
'''

print('==='*15)
print('EXERCICIOS 82'.center(45))
print('==='*15)
print(' ')

lista_total = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um número: '))
    lista_total.append(num)

    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

    escolha = input('Quer continuar? [S/N]').strip().upper()
    if escolha == 'N':
        break

print(f"A lista total:\n\033[32m{lista_total}\033[m")
print('-=-'*5)
print(f'A lista par é:\n\033[32m{lista_par}\033[m')
print('-=-'*5)
print(f'A lista impar é:\n\033[32m{lista_impar}\033[m')
print('-=-'*5)