'''
CRIE UM PROGRAMA ONDE O USUARIO POSSA DIGITAR VARIOS VALORES NÚMERICOS E CADASTRE-OS EM UMA LISTA.
CASO O NÚMERO JÁ EXISTA NA ISTA, ELE NÃO SERA ADICIONADO. NO FINAL, SERA EXIBIDO TODOS OS VALORES DIGITADOS EM ORDEM CRESCENTE
'''

print('==='*15)
print('EXERCICIOS 79'.center(45))
print('==='*15)
print(' ')

lista_num = []

while True:

    num = int(input('Digite um número: '))
    if num not in lista_num:
        lista_num.append(num)
    else:
        print('Esse número já foi cadastrado!')

    cont = input('Quer continuar cadastrando número: [S/N]').strip().upper()
    if cont == 'N':
        break

print(sorted(lista_num))