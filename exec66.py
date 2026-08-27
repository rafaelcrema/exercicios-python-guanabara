'''
CRIE UM PROGRAMA QUE LEIA N NUMEROS INTEIROS PELO TECLADO. PROGRAMA SO PARA QUANDO O USUARIO APERTAR 999
NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL A SOMA ENTR ELES (SEM CONTAR O FLAG)
'''

print('==='*15)
print('EXERCICIOS 66'.center(45))
print('==='*15)
print(' ')

lista_numeros= []
contador = 0


while True:
    num = int(input('Digite um número: \n>'))
    
    if num == 999:
        break

    contador += 1
    lista_numeros.append(num)

soma = sum(lista_numeros)

print(f'\nA quantidade de números escolhidos foram \033[36m{contador}\033[m')
print(f'on números digitados foram \033[36m{lista_numeros}\033[m')
print(f'A soma entre eles foi \033[36m{soma}\033[m')
