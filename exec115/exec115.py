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
    print('MENU PRINCIPAL'.center(44))
    print('==='*15)
    print()

    escolha = input('''
1- CADASTRAR PESSOA
2- VERIFICAR LISTAS DE CADASTRO
3- SAIR
''')

    if escolha == '1':
        funcoes.cadastrar()

    if escolha == '2':
        funcoes.cadastrados()

    if escolha == '3':
        break
