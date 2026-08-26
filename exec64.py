'''
CRIE UM PROGRAMA QUE LEIA VARIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ  VAI PARAR QUANDO O USUARIO DIGITAR 999
NO FINAL, MOSTRE QUANJTOS NÚMEROS FORAM DIGITADIS E QUAL FOI A SOMA ENTRE ELES. DESCONSIDERANDO O 999
'''

print('==='*15)
print('EXERCICIOS 64'.center(45))
print('==='*15)
print(' ')

condicao = 0
soma_digitadis = 0
lista_digitados = []

while condicao != 999:
    num = int(input('Digite um número: \n>'))
    soma_digitadis += 1
    lista_digitados.append(num)

    if num == 999:
        break

    condicao_2 = input('Quer continuar digitando números? [S/N]').upper()

    if condicao_2 == 'S':
        continue
    else:
        break

soma = sum(lista_digitados)
divisao = soma / soma_digitadis

print(f'A quantidade de números digitados foi \033[32m{soma_digitadis}\033[m')
print(f'E a média é: \033[32m{divisao:.2f}\033[m')