'''
CREI UM PEQUENO SISTEMA MODULARIZADO QUE PERMITE CADASTRAR PESSOAS PELO SEU NOME E IDADE EM UM ARQUIVO DE TEXTO SIMPLES

O SISTEMA SÓ VAI TER 2 OPÇÕES: CADASTRAR UMA NOVA PESSOA 
E LISTAR TODAS AS PESSOAS CADASTRADAS.
'''

print('==='*15)
print('EXERCICIOS 115'.center(44))
print('==='*15)
print(' ')

import funcoes
import listacadastro

listacadastro.carregar()


while True:
    print('==='*15)
    print('\033[0;32mMENU PRINCIPAL\033[m'.center(53))
    print('==='*15)
    print()

    escolha = input('''
\033[0;33m1\033[m\033[0;34m -\033[m \033[0;32mCADASTRAR PESSOA\033[m
\033[0;33m2\033[m\033[0;34m -\033[m \033[0;32mVERIFICAR LISTAS DE CADASTRO\033[m
\033[0;33m3\033[m\033[0;34m -\033[m \033[0;32mSAIR\033[m
''')

    if escolha == '1':
        funcoes.cadastrar()

    if escolha == '2':
        funcoes.cadastrados()

    if escolha == '3':
        break
