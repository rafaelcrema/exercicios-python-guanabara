'''
DESENVOLVA UMA LOGICA QUE LEIA O PESO A ALTURA DE UMA PESSOA E CALCULE O SEU IMC DE MOSTRE SEU ESTATUS DE ACORDO
COM A TABELA ABAICO
- ABAIXO DE 18.5 AVAIXO DO PESO
- ENTRE 18.5 E 25 PESO IDEAL
- 25 ATÉ 30 SOBREPESO
- 30 ATÉ 40 OBESIDADE
- ACIMA DE 40: OBSIDADE MORBIDA
'''

print('''
==========================================
            EXERCICIO 43
                IMC
==========================================               
''')
print(' ')

peso = float(input('Digite o seu peso: \n>'))
altura = float(input('Digite sua altura: \n>'))

imc = peso // (altura * altura)

if imc < 18.5:
    print('Seu IMC é \033[31m{}\033[m Muito abaixo do peso ideial'.format(imc))

elif imc >= 18.5 and imc < 25:
    print('Seu IMC é \033[32m{}\033[m. Você esta no peso ideial'.format(imc))

elif imc >= 25 and imc < 30:
    print('Seu IMC é \033[33m{}\033[m. Você esta com sobrepeso'.format(imc))

elif imc >= 30 and imc < 40:
    print('Seu IMC é \033[31m{}\033[m. Você esta com Obsidade'.format(imc))

else:
    print('Seu IMC é \033[31m{}\033[m. Você esta com Obsidade Morbida'.format(imc))