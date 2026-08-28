'''
CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VARIOS PRODUTOS
O PROGRAMA DEVERÁ PERGUNTAR SE O USUARIO VAI CONTINUAR.
NO FINAL, MOSTRE:
[A]QUAL É O TOTAL GASTO NA COMPRA
[B]QUANTOS PRODUTOS CUSTAM MAIS QUE R$ 1000,00
[C]QUAL O NOME DO PRPDUTO MAIS BARATO
'''

print('==='*15)
print('EXERCICIOS 70'.center(45))
print('==='*15)
print(' ')

print("="*12)
print("MERCADINHO")
print("="*12)
print()

lista_nome_produtos = []
lista_preco_produtos = []
produtos_mais = 0
produtos_barato = ''
preço_barato = 999

#while de add preço nome
while True:
    nome = input('Digite o nome do produto: ').capitalize()
    preco = float(input('Digite o preço do produto: '))

    lista_nome_produtos.append(nome)
    lista_preco_produtos.append(preco)

    if preco >= 1000.0:
        produtos_mais +=1
    if preco < preço_barato:
        preço_barato = preco
        produtos_barato = nome
  
    proximo = input('Quer continuar cadastrando produtos? [S/N]').strip().upper()
    if proximo == 'S':
        continue
    elif proximo == 'N':
        break
print('')
print('\n' + '=' * 35)
print('NOTA DA COMPRA'.center(35))
print('=' * 35)

for nome, preco in zip(lista_nome_produtos, lista_preco_produtos):
    print (f'{nome:.<25}: R${preco:>7.2f}')

total = sum(lista_preco_produtos)
print (f'Total: R${total:.2f}')
print(f'{produtos_mais} custaram mais de R$ 1000,00')
print(f'{produtos_barato} foi o produtos mais barato da compra')

print('\n' + '=' * 35)
print('MERCADO CREMA'.center(35))
print('=' * 35)


