'''
CRIE UM PROGRAMA QUE TENHA A FUNÇÃO leiaint(), que vai funcionar de forma
semelhante à função input() do python, só que fazendo a validação
para aceitar apenas um valor numérico.
ex.: n = leiaInt('Digite um n')
'''

print('==='*15)
print('EXERCICIOS 104'.center(44))
print('==='*15)
print(' ')

def leiaInt(num):
    while True:
        n = input('Digite um número: ')
        try:
            num = int(n)
            break
        except ValueError:
            print('\033[31mDigite um número Valido\033[m')

    return num



#CONDIGO PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você digitou o número \033[32m{n}\033[m')