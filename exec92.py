'''
crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos
(com idade) em um dicionario sem por aceso a CTPS for diferente de zero, o dicionario recebera também o ano de contribuição e o salario.
Calcule e acrescente alén da idade com quantos anos a pessoa vai se aposentar.
'''

print('==='*15)
print('EXERCICIOS 92'.center(45))
print('==='*15)
print(' ')

import datetime
import sys

cadastro = {}
ano = datetime.date.today().year

nome = input('Digite o nome: ').strip().capitalize()
cadastro["nome"] = nome

nasc = int(input('Digite seu ano de nascimento: '))
idade = ano - nasc
cadastro['idade'] = idade

carteira = int(input('Digite a sua carteira de trabalho (0 não tem): '))
if carteira == 0:
    print('Vagabundo!')
    sys.exit()

ano_contribuicao = int(input('Digite o ano do seu primeiro trabalho: '))
cadastro['ano de contribuição'] = ano_contribuicao

salario = float(input('Digite o salario: '))
cadastro['salario'] = salario

aposenta_contri = 65 - idade
ano_aposentado = ano + aposenta_contri
ano_trabalho = ano - ano_contribuicao

print('-=-'*30)

if ano_trabalho < 20 and aposenta_contri < 65:
    trabalho_restante = 20 - ano_trabalho
    print(f'Faltam {trabalho_restante} anos de trabalho em carteira e mais {aposenta_contri} anos de trabalho')
    print(f'Se não mudarem, você se aposenta em {ano_aposentado}')
else:
    print(f'Você já é aposentado, sai daqui!!!!')


