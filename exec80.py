'''
crie um programa onde o usuario possa digitar 5 valores númericos e cadastreos em uma lista, já na posição correta
de inserção (sem usar o sort())
no final mosrte a lista ordenada na tela
'''

print('==='*15)
print('EXERCICIOS 80'.center(45))
print('==='*15)
print(' ')

lista_num = []

num_antigo = 0
num_novo = 1

for n in range(5):
    num = int(input('Digite um número: '))
    if not lista_num:
        lista_num.append(num)
        print('Numero cadastrado primero')

    else:
        posicao = 0

        while posicao < len(lista_num):
            if num <= lista_num[posicao]:
                lista_num.insert(posicao, num)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao +=1

        else:
            lista_num.insert(posicao, num)
            print(f'Adicionado na posição {posicao} da lista...')
        posicao +=1

print(lista_num)
