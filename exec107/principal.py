'''
CRIE UM MODULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES INCORPORADAS 
AUMENTAR()
DIMINUIR()
DOBRAR()
METADE()

FAÇA TAMBÉM UM PROGRAMA QUE IMPORTW ESSE MODULO E USE ALGUMAS DESSAS FUNÇÕES

Ex 109
FORMATAR OS VALORES

Ex 110
FUNÇÃO RESUMO QUE TRAZ RESUMO DE VALOR E MELHORA A FORMATAÇÃO DO PROGRAMA
exemplo moeda.resumo(p,80,35)
P = VALOR
80% DE AUMENTO
35% DE REDUÇÃO

Exc 112
Ajustar o codigo, usando replace e try excep
'''

import moeda

print('==='*15)
print('EXERCICIOS 107'.center(44))
print('==='*15)
print(' ')

p = input('Digite o preço: R$ ')
moeda.resumo(p,80,35)
