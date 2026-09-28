'''
CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO()
QUE VAI RECEBER COMO PARMAETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO UM VALOR LITERAL.
INDICANDO SE UMA PESSOA TEM VOTO NEGADO, OCIONAL OU OBRIGATORIO NAS ELEIÇÕES
'''

print('==='*15)
print('EXERCICIOS 101'.center(44))
print('==='*15)
print(' ')

import datetime

#FUNÇÃO
def voto(ano_pessoa):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_pessoa


    if idade < 16:
        return print(f'Você tem {idade} anos e não pode votar!')

    elif idade <= 17 or idade >= 70:
        return print(f'Você tem {idade} anos e pode escolher votar ou não!')

    else:
        return print(f'Você tem {idade} anos e é obrigado a votar')



    

#CODIGO PRINCIPAL
ano_nascimento = int(input('Qual seu ano de nascimento: '))
resultado = voto(ano_nascimento)