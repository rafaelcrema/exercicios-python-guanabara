'''
REFORÇA O DESAFIO 51, DANDO O PRIMEIRO TERMO E A RAZAO DE UMA PA. MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE
'''

print('==='*15)
print('EXERCICIOS 61'.center(45))
print('==='*15)
print(' ')

num = int(input('Primero termo da PA: '))
razao = int(input('De a razão da PA: '))
list_pa = []

term = num
cont = 0

while cont <= 10:
    list_pa.append(term)
    term = term + razao

    cont += 1
print(list_pa)