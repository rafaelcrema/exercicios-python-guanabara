'''
CRIE UM PROGRAMA QUE LEIA VARIOS NÚMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO. MOSTRE A
MÉDIA TODOS ELES PS VALORES E QUAL FOI O MAIOR E O MENOR.
O PROGRAMA DEVE PERGUNTAR AO USUARIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES E QUANDO FALAR NÃO, FAZ O QUE O ENUNCIADO PEDE
'''

print('==='*15)
print('EXERCICIOS 65'.center(45))
print('==='*15)
print(' ')

condicacao = 0
list_num = []
cont = 0

while True:
    num = int(input('Digite um número: \n>'))
    list_num.append(num)

    cont +=1

    condicacao_2 = input('Quer continuar? [S/N]').upper()
    if condicacao_2 == 'S':
        continue
    elif condicacao_2 == 'N':
        break
    else:
        print('Opção errada, animal!!!')
        continue

media = sum(list_num) / cont
maior = max(list_num)
menor = min(list_num)

#print(media, maior, menor)
print(f'O maior número é \033[32m{maior}\033[m')
print(f'O maior número é \033[32m{menor}\033[m')
print(f'A média é \033[32m{media:.2f}\033[m')