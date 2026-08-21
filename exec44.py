'''
elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento

- A VISTA DINHEIRO / CHEQUE 10% DE DESCONTO
- A VISTA NO CARTÃO 5% DE DESCONTO
- EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
- 3X OU MAIS NO CARTÃO 20% DE JUROS
'''

print('''
==========================================
            EXERCICIO 44
        MÉTODOS DE PAGAMENTO
==========================================               
''')
print(' ')

valor_pago = float(input('Digite o valor a ser pago: \n>'))
condicao = input('''
====================
Forma de pagamento:
====================

[1] À Vista no dinheiro ou PIX
[2] À Vista no cartão
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão

''')

if condicao == '1':
    condicao = valor_pago * 0.90
    print('Escolha de pagamento à vista com 10% de desconto R$ {:.2f}'.format(condicao))

elif condicao == '2':
    condicao = valor_pago * 0.95
    print('Escolha de pagamento a vista no carta com 5% de desconto R$ {:.2f}'.format(condicao))

elif condicao == '3':
    condicao = valor_pago / 2
    print('Escolha de pagamento parcelado em 2x de R$ {:.2f} sem juros.'.format(condicao))

elif condicao == '4':
    condicao = valor_pago * 1.20
    print('Escola de pagamento em 3x ou mais com juros de 20%. Valor final de R$ {:.2f}'.format(condicao))

else:
    print('Opção invalida!')