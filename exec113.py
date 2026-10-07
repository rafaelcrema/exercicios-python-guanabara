'''
104.>
CRIE UM PROGRAMA QUE TENHA A FUNÇÃO leiaint(), que vai funcionar de forma
semelhante à função input() do python, só que fazendo a validação
para aceitar apenas um valor numérico.
ex.: n = leiaInt('Digite um n')

113.>
Reescreva a função leiaint() que fizemos no exec 104, incluindo agora a 
posibilidade da digitação de tipo invalido.
Aproveite e crie uma função leiaFloat() com a mesma funcionalidade
'''

print('==='*15)
print('EXERCICIOS 106'.center(44))
print('==='*15)
print(' ')

def leiaInt(num):
    while True:
        n = input('Digite um número inteiro: ')
        try:
            num = int(n)
            break
        except ValueError:
            print('\033[0;31mDigite um número inteiro valido!\033[m')

    return num

def leiafloat(num):
    while True:
        n = input('Digite um número Real: ').replace(',','.')
        try:
            num = float(n)
            break
        except ValueError:
            print('\033[0;31mDigite um número real valido!\033[m')
        
    return num


#CONDIGO PRINCIPAL
n = leiaInt('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')

print(f'Você digitou o número \033[32m{n}\033[m')
print(f'Você digitou o número \033[0;32m{f}\033[m')