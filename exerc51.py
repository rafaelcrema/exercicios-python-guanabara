'''
DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO DE UM 
PROGREÇÃO ARITIMETICA. NO FINAL, MOSTRAR OS 10 PRIMEROS TERMOS DESSA PROGRESSÃO
'''


print('==='*15)
print('EXERCICIOS 51'.center(45))
print('==='*15)
print(' ')

primeiro = int(input('Digite o primeiro número: \n>'))
razao = int(input('Digite a razão: \n>'))
decimo = primeiro + (10 - 1)

for c in range(primeiro, decimo + 1, razao):
    print(c)