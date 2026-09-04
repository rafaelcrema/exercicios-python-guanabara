'''
crie um programa onde o usuario difite uma expreção qualquer que use parametros.
Seu aplicativo deverá analisar se a expressão passada esta com os parametros abertos e fechados na ordem correta
'''

print('==='*15)
print('EXERCICIOS 83'.center(45))
print('==='*15)
print(' ')

aberto = 0
expre = False

conta = input('Digite uma expreção matematica: \n>')

for v in conta:         
    if v == '(':
       aberto +=1
    if v == ')':
        aberto -=1
    if aberto < 0:
        expre = True

if expre:
    print('Expressão errada')

elif aberto < 0: 
    print('Expressão errada!')

elif aberto == 0:
    print(f'Expressão correta: {conta}')

else:
    print(f'Expressão errada: {conta}')