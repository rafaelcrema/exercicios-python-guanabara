'''
DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A
SOMA APENAS DAQUELES QUE FORAM PARES. SE O VALOR DIGITADO FOR IMPAR,
DESCONSIDERE
'''


print('==='*15)
print('EXERCICIOS 50'.center(45))
print('==='*15)
print(' ')

#armazena as escolhas do for
num_escolha = []

#repetição de escolha
for n in range(1, 7):
    num = int(input('Digite um número inteiros: \n>'))

    num_escolha.append(num)

pares = []
#repetição para pegar numero pares
for numeros in num_escolha:
    if numeros % 2 == 0:
        pares.append(numeros)

#exibir
print(f'Os números pares escolhidos foram \033[32m{pares}\033[m')

