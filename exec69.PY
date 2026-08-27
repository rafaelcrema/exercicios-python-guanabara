'''
CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VARIAS PESSOAS. 
A CADA PESSOA CADASTRADA, O PROGORMA DEVERÁ PERGUTAR SE O USUARIO QUER OU NÃO CONTINUAR
NO FINAL, MOSTRE:
A] QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
B] QUANTOS HOMENS HOMENS FORAM CADASTRADOS
C]QUANTAS MULHERES TEM MENOS DE 20 ANOS
'''

print('==='*15)
print('EXERCICIOS 69'.center(45))
print('==='*15)
print(' ')

print("="*12)
print("CADASTRO DE CLIENTES")
print("="*12)
print()

homem = 0
maior_all = 0
menor_mulher = 0

while True:
    idade = int(input('Digite a idade da pessoas: \n'))
    sexo = input('Digite o Sexo da pessoa [M/F]: \n').strip().upper()

    if sexo == 'M':
        homem += 1
    if sexo == 'M' or sexo == 'F':
        if idade >= 18:
            maior_all += 1
    if idade < 18:
        if sexo == 'F':
            menor_mulher +=1

    proximo = input('Quer continuar? [S/N]').strip().upper()
    if proximo == 'N':
        break

print(f'Existem \033[35m{maior_all}\033[m pessoas maiores de idade')
print(f'Foram cadastrados \033[35m{homem}\033[m homens!')
print(f'Tem \033[35m{menor_mulher}\033[m mulhers menor de idade')